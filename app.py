import requests
import argparse
from utils import export_to_file

def get_wayback_urls(url):
    wayback_url = f"https://web.archive.org/cdx/search/cdx?url={url}&output=text&fl=original&collapse=urlkey"
    response = requests.get(wayback_url)
    
    if response.status_code == 200:
        urls = response.text.splitlines()
        return urls
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description='Wayback Machine URL Extractor')
    parser.add_argument('--url', required=True, help='The URL pattern (e.g., "*.example.com/*")')
    parser.add_argument('--output', help='Output file to save the results')
    
    args = parser.parse_args()
    
    urls = get_wayback_urls(args.url)
    
    if urls:
        print(f"Found {len(urls)} archived URLs for {args.url}:\n")
        for u in urls:
            print(u)
        
        # If output file is specified, export results to file
        if args.output:
            export_to_file(urls, args.output)
            print(f"\nURLs saved to {args.output}")
    else:
        print("No URLs found or an error occurred.")

if __name__ == "__main__":
    main()
