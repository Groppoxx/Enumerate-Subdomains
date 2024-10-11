import requests
import sys
import pyfiglet

subDomains = []

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        subdomains = set()

        for entry in data:
            names = entry.get('name_value')

            if names:
                for name in names.split('\n'):
                    name = name.lower()
                    if '*' not in name and name.endswith(f".{domain}"):
                        subdomains.add(name)
        return sorted(subdomains)

    except Exception as exc:
        print(f"Error trying to get subdomains: {exc}")
        return []

def main():
    ascii_banner = pyfiglet.figlet_format("Enumerate Subdomains")
    print(ascii_banner)

    if len(sys.argv) != 2:
        print("Usage: python enumsbdm.py <dominio>")
        sys.exit(1)

    domain = sys.argv[1].strip().lower()

    print(f"Searching subdomains from: {domain}\n")
    global subDomains
    subDomains = get_subdomains(domain)

    if subDomains:
        for sub in subDomains:
            print(sub)
        print(f"\nAmount of subdomains found ({len(subDomains)})")

    else:
        print("Subdomains not found")

if __name__ == "__main__":
    main()
