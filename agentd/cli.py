#!/usr/bin/env python3
import argparse
from agentd.runtime.version import RUNTIME_VERSION

def main():
    parser = argparse.ArgumentParser(description="agentd CLI - runtime interface")
    parser.add_argument("--version", action="store_true", help="Show runtime version")
    parser.add_argument("command", nargs="?", help="Command to run (e.g. trace)")
    parser.add_argument("--input", help="Input file for command")

    args = parser.parse_args()

    if args.version:
        print("agentd runtime version:", RUNTIME_VERSION)
    elif args.command == "trace":
        print("Tracing (placeholder)... input =", args.input)
    else:
        print("agentd CLI placeholder. Use --version or trace [--input file]")

if __name__ == "__main__":
    main()
