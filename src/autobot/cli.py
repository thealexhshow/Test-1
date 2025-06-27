#!/usr/bin/env python3
import argparse
from .core import ask

parser = argparse.ArgumentParser(description="Ask OpenAI quickly from the CLI")
parser.add_argument("prompt", nargs="+", help="Prompt to send")
args = parser.parse_args()
print(ask(" ".join(args.prompt)))
