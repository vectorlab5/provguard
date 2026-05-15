from provguard.core.registration import EvidenceRegister
from provguard.core.retrieval import HybridRetriever, ProvenanceReranker
from provguard.core.generation import GroundedGenerator, ClaimDecomposer
from provguard.core.verification import SemanticVerifier
from provguard.core.audit import AuditManager
from typing import List, Dict, Any, Tuple
import time

class ProvGuardRAG:
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.register = EvidenceRegister()
        self.retriever = HybridRetriever()
        self.reranker = ProvenanceReranker()
        self.generator = GroundedGenerator()
        self.decomposer = ClaimDecomposer()
        self.verifier = SemanticVerifier()
        self.audit_manager = AuditManager()
        
        # Mock source metadata
        self.source_metadata = {
            "ton_iot": {"auth": 0.9, "hist": 0.85},
            "ciciot": {"auth": 0.8, "hist": 0.75},
            "cve": {"auth": 1.0, "hist": 0.95},
            "mitre": {"auth": 1.0, "hist": 0.98}
        }

    def process_query(self, query: str) -> Dict[str, Any]:
        """End-to-end query processing (Algorithm 1)."""
        start_time = time.time()
        
        # Stage 2: Retrieval & Reranking
        raw_evidence = self.retriever.retrieve(query)
        # Mocking some evidence for demonstration if retriever is empty
        if not raw_evidence:
            raw_evidence = [
                {"content": "Device D17 saw SYN flood at 14:17.", "src": "ton_iot", "tau": time.time() - 3600, "relevance_score": 0.9},
                {"content": "MITRE T1498 describes DDoS attacks.", "src": "mitre", "tau": time.time() - 10**6, "relevance_score": 0.8}
            ]
        
        reranked_evidence = self.reranker.rerank(query, raw_evidence, self.source_metadata)
        top_k_evidence = reranked_evidence[:5] # k=5
        
        # Stage 3: Generation & Decomposition
        answer = self.generator.generate_answer(query, top_k_evidence)
        claims = self.decomposer.decompose(answer)
        
        # Stage 4: Verification
        verification_results = self.verifier.verify_claims(claims, top_k_evidence)
        
        # Stage 5: Audit
        retrieval_data = {
            "snapshot_id": "snap_2026_05_15",
            "k": len(top_k_evidence),
            "evidence": [{"h": e.get("h", "mock_hash"), "src": e["src"], "tau": e["tau"]} for e in top_k_evidence]
        }
        
        inference_config = {
            "model_id": self.generator.model_name,
            "prompt_hash": "abc123hash",
            "alpha": self.reranker.alpha,
            "beta": self.reranker.beta
        }
        
        manifest = self.audit_manager.construct_manifest(
            query, retrieval_data, inference_config, verification_results, answer
        )
        h_m, pos = self.audit_manager.anchor_manifest(manifest)
        proof = self.audit_manager.get_inclusion_proof(pos)
        
        latency = (time.time() - start_time) * 1000 # ms
        
        return {
            "answer": answer,
            "claims": verification_results,
            "manifest": manifest,
            "h_m": h_m,
            "pos": pos,
            "proof": proof,
            "latency_ms": latency
        }
