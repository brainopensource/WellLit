from utils.auxiliary.queries import get_with_retries
from utils.connectors.app_urls import WOODMAC_FIELD_MONTHLY_PRODUCTION
import requests
from requests.auth import HTTPBasicAuth
import time
import json
import os


def fetch_production_data(username, password):
    response = get_with_retries(WOODMAC_FIELD_MONTHLY_PRODUCTION, username, password)
    return response.get("value", []) if response else []


# Function to handle the pagination of OData API
def fetch_all_data(username, password, odata_url=WOODMAC_FIELD_MONTHLY_PRODUCTION):
    """
    Fetches all data from the OData API, handling pagination.
    Returns a list of all results.
    """
    all_data = []
    # Define parameters for the first request
    params = {
        "$select": "field_code,_field_name,production_period,oil_production_kbd,gas_production_mmcfd",}
    
    # Initial request to fetch data
    data = get_with_retries(odata_url, username, password, params)
    
    if "error" not in data:
        all_data.extend(data.get('value', []))
        
        # Check for pagination and continue fetching until all pages are retrieved
        while '@odata.nextLink' in data:
            next_url = data['@odata.nextLink']
            print(f"Fetching next page of data from: {next_url}")
            data = get_with_retries(next_url, username, password, params)
            
            if "error" not in data:
                all_data.extend(data.get('value', []))
            else:
                break

    print('saving all data to file')
    #save_to_file(all_data)
    return all_data


def save_to_file(data):
    output_path = os.path.join(os.getcwd(), "full_production_data.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Full data saved to {output_path}")
