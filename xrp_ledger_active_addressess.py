import requests
from datetime import datetime, timedelta

# Define the time frame (24 hours ago from now)
time_limit = (datetime.now() - timedelta(hours=24)).isoformat() + "Z"

# Define the API endpoint (Ripple Data API)
api_url = "http://data.ripple.com/v2/active_accounts/XRP/USD+rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B"

# Define the parameters for the GET request
params = {
    "start": time_limit,
    "interval": "hour",
    "descending": False
}

# Send the GET request
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Check if 'accounts' key exists in the data
    if 'accounts' in data:
        # Access the 'accounts' key
        accounts = data['accounts']

        # Calculate the number of unique accounts
        num_unique_accounts = len(accounts)

        # Print the number of unique accounts
        print(f'Number of unique accounts: {num_unique_accounts}')
    else:
        print("'accounts' key not found in the data.")
else:
    print("Failed to fetch data from the Ripple Data API.")