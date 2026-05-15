import hashlib
import time
from typing import Dict, Any

class EvidenceRegister:
    def __init__(self):
        pass

    @staticmethod
    def compute_hash(content: str) -> str:
        """Compute SHA-256 hash of document content."""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def register_document(self, content: str, source_id: str, parser_version: str = "v1.0") -> Dict[str, Any]:
        """
        Register a document with provenance metadata.
        Returns the metadata dictionary.
        """
        doc_hash = self.compute_hash(content)
        timestamp = time.time()
        
        metadata = {
            "src": source_id,
            "tau": timestamp,
            "parser": parser_version,
            "h": doc_hash
        }
        
        return metadata

    def verify_integrity(self, content: str, registered_hash: str) -> bool:
        """Verify that the content matches the registered hash."""
        return self.compute_hash(content) == registered_hash
