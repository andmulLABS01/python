import json

health_data = """
{
  "Checks": [
    {
      "Name": "Connections",
      "Status": "Healthy"
    },
    {
      "Name": "ConnectionRead",
      "Status": "unHealthy"
    },
    {
      "Name": "redis",
      "Status": "Healthy"
    },
    {
      "Name": "ProcessCheck",
      "Status": "Healthy"
    },
    {
      "Name": "UserProfile",
      "Status": "unHealthy"
    },
    {
      "Name": "features",
      "Status": "unHealthy",
      "Description": "sample sample sample"
    },
    {
      "Name": "shutdown",
      "Status": "Healthy"
    },
    {
      "Name": "lifespan",
      "Status": "unHealthy"
    }
  ]
}

"""

# make a function that will output the number of healthy and unhealthy checks
# Make a function that will output the names of unhealthy checks

#format your JSON String to load like json
given_json = json.loads(health_data)

#function that will output the number of healthy and unhealthy checks
def count_Status(given_json):
# Count the occurrences of "Healthy" and "unHealthy" values
  count_healthy = 0
  count_unhealthy = 0

# Go through the dictionary and count using a for loop with if elif statements
  for item in given_json["Checks"]:
    status = item.get("Status")
    if status == "Healthy":
        count_healthy += 1
    elif status == "unHealthy":
        count_unhealthy += 1

  print("Number of 'Healthy' checks:", count_healthy)
  print("Number of 'unHealthy' checks:", count_unhealthy)
  #print("")

#function that will output the names of unhealthy checks
def print_Names(given_json):
  for item in given_json["Checks"]:
    status = item.get("Status")
    if status == "unHealthy":
        name = item.get("Name")
        print(f"Name: {name}")



print(count_Status(given_json))
print(print_Names(given_json))
