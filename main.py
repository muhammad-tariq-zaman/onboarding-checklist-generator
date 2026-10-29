"""Generate an onboarding checklist from a role template (JSON).

Usage: python3 main.py template.json --name "Ayesha Khan" --role "IT Support"
Template format: {"common": [...], "IT Support": [...]}
"""
import argparse
import json
import sys


def checklist(template, role):
    items = list(template.get("common", []))
    items += template.get(role, [])
    return items


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template", help="JSON role-template file")
    parser.add_argument("--name", required=True)
    parser.add_argument("--role", required=True)
    args = parser.parse_args(argv)
    with open(args.template, encoding="utf-8") as f:
        template = json.load(f)
    print(f"Onboarding checklist for {args.name} ({args.role}):")
    for i, item in enumerate(checklist(template, args.role), 1):
        print(f"[ ] {i}. {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
