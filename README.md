# ProvGuard-RAG: Trustworthy Retrieval-Augmented Generation for CPS

ProvGuard-RAG is a framework for provenance-aware retrieval-augmented generation (RAG) designed for cyber-physical systems (CPS) incident intelligence. It ensures that model responses are traceable, semantically verified against evidence, and recorded in a tamper-evident audit log.

## Key Features

- **Provenance-Aware Reranking**: Rerank retrieved evidence based on source trust, recency, and historical verification success.
- **Semantic Claim Verification**: Automatically decomposes generated answers into atomic claims and verifies them using a fine-tuned Natural Language Inference (NLI) model.
- **Audit Manifests**: Generates cryptographically hashed manifests for every query, including query hashes, evidence identifiers, and verification labels.
- **Ledger Anchoring**: Anchors manifests in an append-only Merkle transparency log to provide post-hoc verifiability.
- **CPS Telemetry Rendering**: Specialized logic for anonymizing and rendering industrial IoT telemetry into natural language while preserving semantic meaning.

## System Architecture

The ProvGuard-RAG pipeline consists of five stages:
1. **Evidence Registration**: Hashing and metadata tagging of ingestion sources.
2. **Hybrid Retrieval**: Combination of BM25 lexical and dense vector search with provenance-aware reranking.
3. **Grounded Generation**: Response generation conditioned on verified evidence.
4. **Semantic Verification**: Claim-level entailment checking.
5. **Audit Anchoring**: Record creation and Merkle-tree anchoring.

## Installation

```bash
git clone https://github.com/your-repo/provguard-rag.git
cd provguard-rag
pip install -r requirements.txt
```

## Quick Start

### Run a Query
Process a single incident intelligence query through the pipeline:
```bash
PYTHONPATH=. python3 main.py "Was device D17 compromised between 14:00 and 14:30?"
```

### Run Evaluation
Run the built-in benchmarking suite to test robustness and accuracy:
```bash
PYTHONPATH=. python3 provguard/eval/evaluate.py
```

## Configuration

You can customize the reranking behavior and verification thresholds in `provguard/pipeline.py`:
- `alpha`: Relevance weight
- `beta`: Source trust weight
- `gamma`: Recency weight
- `delta`: Verification cascade weight
- `theta_entail`: Confidence threshold for claim support

## License

This project is licensed under the Apache License 2.0.
