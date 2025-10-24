# cli/main.py

import argparse
import json
from fusion_writer.agent import generate_post

def main():
    parser = argparse.ArgumentParser(description="Fusion Writer Agent CLI")
    parser.add_argument("--input", type=str, required=True, help="Path to JSON input file")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        data = json.load(f)

    post = generate_post(data)
    print("\nGenerated Post:\n")
    print(post)

if __name__ == "__main__":
    main()
