
#Import modules  os, requests, json, and csv
import os
import csv
try:
    import requests
except ImportError:
    print("requests module is not installed. Please install it using 'pip install requests'.")
    exit(1)
import json

# Put in the parameters for the API
url = "https://free-nba.p.rapidapi.com/players"

querystring = {"page":"0","per_page":"25"}

headers = {
    'X-RapidAPI-Key': 'INSERT YOUR KEY HERE',
    'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
  }

# Make the API requestpit
try:
    response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful
    if response.status_code == 200:
        try:
            player_data = response.json()

            # Specify the name of the CSV file.
            csv_file = 'nba_players.csv'

            # Extract and format the data
            formatted_data = []
            for player in player_data['data']:
                formatted_data.append({
                    'Player ID': player['id'],
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
        # Add additional error handling     
        except json.JSONDecodeError:
            print("Error: The response does not contain valid JSON data.")
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')


