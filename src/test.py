import requests
from requests.auth import HTTPBasicAuth

# Define the OData service URL and entity endpoint
odata_url = 'https://data.iprod.woodmac.com/query-internal/anp/all/odata/anp__field_monthly_production_aggregation__transform'

# Basic authentication credentials
username = ''  # Replace with your actual username
password = ''  # Replace with your actual password

# Define the query parameters for the initial request
params = {
    "$top": "3",  # Limit to top 10 records (adjust as needed)
    "$select": "field_code,_field_name,data_source,last_updated_on,production_period,oil_production_kbd,gas_production_mmcfd",
    "$orderby": "production_period asc"  # Example ordering
}

# Initialize an empty list to store all the results
all_data = []

# Make the initial request
response = requests.get(odata_url, params=params, auth=HTTPBasicAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Append the current page of results to the all_data list
    all_data.extend(data['value'])
    # Print result to check if we have pagination
    print(data)
    print(data['value'])

    # Check for pagination and continue fetching until all pages are retrieved
    while '@odata.nextLink' in data:
        # Get the nextLink URL from the response
        next_url = data['@odata.nextLink']
        
        # Make the request to the next page of data
        response = requests.get(next_url, auth=HTTPBasicAuth(username, password))
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            all_data.extend(data['value'])  # Append the next page of data to the list
        else:
            print(f"Error {response.status_code}: {response.text}")
            break

else:
    print(f"Error {response.status_code}: {response.text}")

# Now all_data contains all the results from the paginated responses
print(f"Total records retrieved: {len(all_data)}")
print(all_data)  # You can process this data further
