import argparse
import json
from provguard.pipeline import ProvGuardRAG

def main():
    parser = argparse.ArgumentParser(description="ProvGuard-RAG CLI")
    parser.add_argument("query", type=str, help="Incident intelligence query")
    args = parser.parse_args()

    pipeline = ProvGuardRAG()
    result = pipeline.process_query(args.query)

    print("\n=== ProvGuard-RAG Answer ===")
    print(result["answer"])
    
    print("\n=== Claims & Verification ===")
    for c in result["claims"]:
        print(f"- [{c['status'].upper()}] {c['claim']}")
        
    print("\n=== Audit Manifest Hash ===")
    print(result["h_m"])
    print(f"Log Position: {result['pos']}")
    print(f"Latency: {result['latency_ms']:.2f} ms")

if __name__ == "__main__":
    main()
