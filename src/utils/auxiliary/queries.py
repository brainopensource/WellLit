import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
import time


# The function you've provided to get data with retries
def get_with_retries(url, username, password, params, max_retries=2, delay=5):
    """
    Attempts to perform a GET request with basic authentication up to 'max_retries' times.
    Returns the JSON response if status_code is 200.
    Otherwise, returns an error message.
    """
    response = None
    for attempt in range(1, max_retries + 1):
        try:
            print('\n Trying to connect to Woodmac...', url, username)
            response = requests.get(url, params=params, auth=HTTPBasicAuth(username, password))
            print(response, response.status_code, response.text)

            # Check if the response status code is 200
            if response.status_code == 200:
                return response.json()
            else:
                delay = delay + attempt * 3
                print(f"[Attempt {attempt}] Status: {response.status_code} - Retrying in {delay}s...")
                print("\n Delay", delay)
                time.sleep(delay)

        except Exception as e:
            print(f"[Attempt {attempt}] Exception: {e} - Retrying in {delay}s...")
            time.sleep(delay)

    # If all attempts failed, return a structured error message
    if response:
        return {"error": f"Request failed with status code {response.status_code}: {response.text}"}
    else:
        return {"error": "No response received after multiple attempts."}


# Function to handle the pagination of OData API
def fetch_all_data(odata_url, username, password):
    """
    Fetches all data from the OData API, handling pagination.
    Returns a list of all results.
    """
    all_data = []
    # Define parameters for the first request
    params = {
        "$top": "10",  # Limit to top 10 records (adjust as needed)
        "$select": "field_code,_field_name,data_source,last_updated_on,production_period,oil_production_kbd,gas_production_mmcfd",}
    
    # Initial request to fetch data
    data = get_with_retries(odata_url, username, password)
    
    if "error" not in data:
        all_data.extend(data.get('value', []))
        
        # Check for pagination and continue fetching until all pages are retrieved
        while '@odata.nextLink' in data:
            next_url = data['@odata.nextLink']
            print(f"Fetching next page of data from: {next_url}")
            data = get_with_retries(next_url, username, password)
            
            if "error" not in data:
                all_data.extend(data.get('value', []))
            else:
                break
    return all_data
