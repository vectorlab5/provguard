import hashlib
import json
import time
from typing import List, Dict, Any, Tuple

class MerkleTree:
    def __init__(self, leaves: List[str]):
        self.leaves = [hashlib.sha256(l.encode()).hexdigest() for l in leaves]
        self.tree = self._build_tree(self.leaves)

    def _build_tree(self, nodes: List[str]) -> List[List[str]]:
        tree = [nodes]
        while len(nodes) > 1:
            if len(nodes) % 2 != 0:
                nodes.append(nodes[-1])
            new_level = []
            for i in range(0, len(nodes), 2):
                combined = nodes[i] + nodes[i+1]
                new_level.append(hashlib.sha256(combined.encode()).hexdigest())
            tree.append(new_level)
            nodes = new_level
        return tree

    def get_root(self) -> str:
        return self.tree[-1][0] if self.tree else ""

    def get_audit_path(self, index: int) -> List[Tuple[str, str]]:
        path = []
        for level in self.tree[:-1]:
            if index % 2 == 0:
                sibling_index = index + 1
                direction = "right"
            else:
                sibling_index = index - 1
                direction = "left"
            path.append((level[sibling_index], direction))
            index //= 2
        return path

    @staticmethod
    def verify_path(leaf_hash: str, path: List[Tuple[str, str]], root: str) -> bool:
        current_hash = leaf_hash
        for sibling_hash, direction in path:
            if direction == "right":
                combined = current_hash + sibling_hash
            else:
                combined = sibling_hash + current_hash
            current_hash = hashlib.sha256(combined.encode()).hexdigest()
        return current_hash == root

class AuditManager:
    def __init__(self):
        self.manifest_history = []
        self.merkle_tree = None

    def construct_manifest(
        self,
        query: str,
        retrieval_data: Dict[str, Any],
        inference_config: Dict[str, Any],
        verification_results: List[Dict[str, Any]],
        output: str
    ) -> Dict[str, Any]:
        """Eq. 7: Construct the five-record audit manifest."""
        h_q = hashlib.sha256(query.encode()).hexdigest()
        h_a = hashlib.sha256(output.encode()).hexdigest()
        
        manifest = {
            "Q": {
                "h_q": h_q,
                "t_query": time.time(),
                "user_id": "system"
            },
            "R": retrieval_data,
            "I": inference_config,
            "V": {
                "verifications": verification_results,
                "flag_policy": "standard"
            },
            "O": {
                "h_a": h_a,
                "t_response": time.time(),
                "env_metadata": {"version": "1.0"}
            }
        }
        return manifest

    def anchor_manifest(self, manifest: Dict[str, Any]) -> Tuple[str, int]:
        """Anchor the manifest hash in a local Merkle tree (mock ledger)."""
        manifest_str = json.dumps(manifest, sort_keys=True)
        h_m = hashlib.sha256(manifest_str.encode()).hexdigest()
        
        self.manifest_history.append(h_m)
        self.merkle_tree = MerkleTree(self.manifest_history)
        
        pos = len(self.manifest_history) - 1
        return h_m, pos

    def get_inclusion_proof(self, pos: int) -> Dict[str, Any]:
        """Get Merkle audit path for a manifest at a given position."""
        if not self.merkle_tree:
            return {}
        
        return {
            "root": self.merkle_tree.get_root(),
            "path": self.merkle_tree.get_audit_path(pos)
        }
