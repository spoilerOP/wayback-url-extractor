# Wayback URL Extractor

The **Wayback URL Extractor** is a simple Python tool that allows you to extract archived URLs from the [Wayback Machine](https://archive.org/web/). It fetches URLs that match a given pattern using the Wayback Machine's CDX API.

## Features
- Extracts archived URLs from the Wayback Machine.
- Supports URL patterns with wildcards (e.g., `*.example.com/*`).
- Saves results to a text file for easy access.

## Prerequisites
- Python 3.x
sudo apt install python3-venv

## Create a virtual environment in the project directory:

bash
Copy code
python3 -m venv venv

## Activate the virtual environment:

bash
Copy code
source venv/bin/activate 
- `requests` module (to install it, use `pip install requests`)
## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/spoilerOP/wayback-url-extractor.git


## Navigate to the project folder:

bash
Copy code
cd wayback-url-extractor



## Create and activate a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


## Install the required dependencies:

bash
Copy code
pip install -r requirements.txt


## Usage
To use the Wayback URL Extractor, run the following command:
python app.py --url "*.example.com*" --output deakins.txt



