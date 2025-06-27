#!/usr/bin/env python3
import argparse
from autopilot.agent import ask

def main() -> None:
    parser = argparse.ArgumentParser(description="Ask GPT-4o from the terminal")
    parser.add_argument("prompt", nargs="+", help="Your question")
    args = parser.parse_args()
    print(ask(" ".join(args.prompt)))

if __name__ == "__main__":
    main()
