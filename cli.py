import argparse
from seekfind import lookup, check, breach  # import the breach module

def main():
    parser = argparse.ArgumentParser(description="seekfind osint cli")
    subparsers = parser.add_subparsers(dest="command")

    # WHOIS lookup
    lookup_parser = subparsers.add_parser("lookup", help="run WHOIS lookup")
    lookup_parser.add_argument("-d", "--domain", required=True, help="target domain")

    # Social media handle check
    check_parser = subparsers.add_parser("check", help="check handle availability")
    check_parser.add_argument("-u", "--username", required=True, help="target username")

    # Email breach check
    breach_parser = subparsers.add_parser("breach", help="check if email was breached")
    breach_parser.add_argument("-e", "--email", required=True, help="email address to check")

    args = parser.parse_args()

    if args.command == "lookup":
        lookup.run(args.domain)
    elif args.command == "check":
        check.run(args.username)
    elif args.command == "breach":
        breach.run(args.email)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
