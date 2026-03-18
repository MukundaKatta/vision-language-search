"""CLI for vision-language-search."""
import sys, json, argparse
from .core import VisionLanguageSearch

def main():
    parser = argparse.ArgumentParser(description="Multimodal search engine combining vision and language understanding")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = VisionLanguageSearch()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.search(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"vision-language-search v0.1.0 — Multimodal search engine combining vision and language understanding")

if __name__ == "__main__":
    main()
