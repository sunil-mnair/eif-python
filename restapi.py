import requests

# Define the API endpoint
url = 'https://eif.pythonanywhere.com/countries'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    countries = response.json()
    # Print the retrieved data
    for country in countries:
        print(f"Name: {country['name']}, Capital: {country['capital']}")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")