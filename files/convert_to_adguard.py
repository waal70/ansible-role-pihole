"""Module providing a function to convert pihole adlists to adguard format."""
import sys
import json
import yaml


def convert_adlists(adlists_json):
    """Convert Pi-hole adlists to AdGuard Home filters format."""
    try:
        adlists_data = json.loads(adlists_json)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in adlists data", file=sys.stderr)
        sys.exit(1)

    filters = []
    for i, adlist in enumerate(adlists_data, start=1):
        # Extract relevant data from Pi-hole adlist
        address = adlist.get('address')
        enabled = adlist.get('enabled', 0) == 1
        comment = adlist.get('comment', '')

        # Create AdGuard Home filter entry
        filter_entry = {
            'enabled': enabled,
            'url': address,
            'name': comment if comment else f"Pi-hole List {i}",
            'id': i
        }
        
        filters.append(filter_entry)

    return {'filters': filters}

def main():
    """Function performing the conversion."""
    if len(sys.argv) != 2:
        print("Usage: python3 convert_to_adguard.py myadlist.json > adguard_filters.yaml")
        sys.exit(1)

    adlists_file = sys.argv[1]

    # Read Pi-hole adlists
    try:
        with open(adlists_file, 'r', encoding="utf-8") as f:
            adlists_json = f.read()
    except FileNotFoundError:
        print(f"Error: Pi-hole adlists file {adlists_file} not found", file=sys.stderr)
        sys.exit(1)

    # Convert and output
    config = convert_adlists(adlists_json)
    print(yaml.dump(config, default_flow_style=False))

if __name__ == "__main__":
    main()
