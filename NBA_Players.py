
#Import modules  os, requests, json, and csv
import os
import csv
import requests
import json

# Put in the paramitors for the API
url = "https://free-nba.p.rapidapi.com/players"

querystring = {"page":"0","per_page":"25"}

headers = {
    'X-RapidAPI-Key': '6fea4a232bmshb8ebb4116ed874bp179727jsn3a44b6c19b44',
    'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
  }

# Make the API request
response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    try:
        player_data = response.json()

        # Define the CSV file name
        csv_file = 'nba_players.csv'

        # Extract and format the data
        formatted_data = []
        for player in player_data:
            formatted_data.append({
                'Player ID': player[id],
                'First Name': player['first_name'],
                'Last Name': player['last_name'],
                'Position': player['position'],
                'Team Name': player['team']['full_name']
            })

        # Write the data to a CSV file
        with open(csv_file, 'w', newline='') as csvfile:
            fieldnames = ['Player ID', 'First Name', 'Last Name', 'Position', 'Team Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(formatted_data)

        print(f'Data has been saved to {csv_file}')
    # put in Error checking for exceptions
    except requests.exceptions.JSONDecodeError:
        print("Error: The response does not contain valid JSON data.")
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
# for i in flight['data']:
#     if i['depart_date'] == "s":


# drew = json.loads(strin)

# for i in drew['Reservations']:
#     id = i['Instances'][0]['InstanceId']
#     print(f'instance number: {id}')

# print(drew['Reservations'][0]['Instances'][0]['InstanceId'])
# print(drew['Reservations'][1]['Instances'][0]['InstanceId'])
# print(drew['Reservations'][2]['Instances'][0]['InstanceId'])
# print(drew['Reservations'][3]['Instances'][0]['InstanceId'])
# print('------------------------------------------------------------------')
# print((drew['Reservations'][0]))
# print(response.text)
