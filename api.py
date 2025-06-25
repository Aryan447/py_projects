# import requests

# url = "https://catfact.ninja/fact"

# response = requests.get(url)
# print(response.status_code)
# data = response.json()
# print(data['fact'])

import requests
# API endpoints
url = 'https://api.genderize.io?name='
nationality_url = "https://api.nationalize.io/?name="

# Get user input
name = input("Please enter your name: ")

# Fetch gender data
response = requests.get(url + name)
data = response.json()

# Fetch nationality data
nationresponse = requests.get(nationality_url + name)
nationdata = nationresponse.json()

# Print gender
print("Predicted Gender:", data.get('gender', 'Not available'))

# Check and print nationality
if nationdata['country']:
    country_id = nationdata['country'][0]['country_id']
    if country_id == 'IN':
        print("You might be Indian.")
    print("You might be from:", country_id)
else:
    print("Nationality could not be predicted.")
