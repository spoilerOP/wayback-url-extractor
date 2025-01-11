import requests
import argparse
import json
import re

def get_wayback_urls(url, output_file):
    # Define the Wayback Machine URL
    wayback_url = f"http://archive.org/wayback/available?url={url}"

    # Send a request to Wayback Machine to check for available snapshots
    response = requests.get(wayback_url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()

        # Check if there are any available snapshots
        if "archived_snapshots" in data and "closest" in data["archived_snapshots"]:
            print(f"Found snapshots for: {url}")

            # Extract URLs from the snapshots
            snapshot_url = data["archived_snapshots"]["closest"]["url"]
            print(f"Snapshot URL: {snapshot_url}")

            # Save the snapshot URL to the output file
            with open(output_file, "w") as file:
                file.write(f"Snapshot URL: {snapshot_url}\n")

        else:
            print(f"No snapshots found for: {url}")
            with open(output_file, "w") as file:
                file.write("No snapshots found.\n")

    else:
        print(f"Error: Could not retrieve data from Wayback Machine for {url}")
        with open(output_file, "w") as file:
            file.write(f"Error retrieving data from Wayback Machine for {url}\n")

def main():
    parser = argparse.ArgumentParser(description="Wayback URL Extractor")
    parser.add_argument('--url', type=str, required=True, help="The URL to search in the Wayback Machine.")
    parser.add_argument('--output', type=str, required=True, help="The output file to save the results.")
    
    args = parser.parse_args()

    # Call the function to get URLs from Wayback Machine
    get_wayback_urls(args.url, args.output)

if __name__ == "__main__":
    main()
