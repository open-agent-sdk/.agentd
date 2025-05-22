#!/usr/bin/env python3

import argparse
import sys

def init():
    print("Initializing agent coordination scaffold...")
    # Placeholder: setup directories, schema files, runtime config
    # Future: connect to schema registry or local fallback logic
    print("Done. Project scaffold ready.")

def fallback():
    print("Fallback handler not yet implemented.")
    # Placeholder for fallback routing logic
    # Future: detect and log tool/intent failures
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="agentd: Coordination scaffolding CLI for agent workflows"
    )

    subparsers = parser.add_subparsers(dest="command")

    parser_init = subparsers.add_parser("init", help="Initialize a new agent project")
    parser_fallback = subparsers.add_parser("fallback", help="Trigger fallback behavior")

    args = parser.parse_args()

    if args.command == "init":
        init()
    elif args.command == "fallback":
        fallback()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
