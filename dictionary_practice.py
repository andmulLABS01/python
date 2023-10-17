# #### Dictionaly and JSON #####

import json

# #Sample dictionalry
# old_data = {"President": "Barack Obama", "President2": "George Washington"}

# data = { "President": {
#             "name": "Barack Obama",
#             "number": "44"
#         }
# }

# print(type(data))

# #To access itmes in a dictionary we use [] but with a key
# print(data["President"])

# print(old_data["President"])
# print(old_data["President2"])


# #To access itmes in a list we use [] and index positions
# someList = ["tylong", "kingman"]
# print(someList[0])

# #####Converting Dictonary to a String #####  *json.dumps* 

# json_string = json.dumps(data)
# print(json_string)
# print(type(json_string))

# #format your JSON String to look like json
# json_formattted_string = json.dumps(data,  indent=4)
# print(json_formattted_string)
# print(type(json_formattted_string))

# #Taking Dictionary and creating a JSON file
# print("Taking Dictionary and creating a JSON file")
# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file, indent=4)


# #Seseriliation, Converting JSON to a Dictionary

# print("Taking JSON file and creating a Dictionary")
# with open("data_file.json", "r") as read_file:
#     dataV2 = json.load(read_file)

# print(type(dataV2))
# print(dataV2)


# print("Parsing Through dictionary and JSON")

# example = {
#   "Teams":[
#     {"Giants":[{"wins":4}, {"losses":1}]},
#     {"Patriots":[{"wins":2}, {"losses":3}]},
#     {"Chiefs":[{"wins":4}, {"losses":1}]}
#   ]
# }

# print(example["Teams"])
# print(type(example["Teams"]))

# print(example["Teams"][0])
# print("access the worst teams win loss")

# print(example["Teams"][1]["Patriots"])
# print(type(example["Teams"][1]["Patriots"]))

# #write a line of cod that will print just the number of winds for the best team

# print(example["Teams"][0]["Giants"][0]["wins"])

# #challenge 2 Parse Status JSOM

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
  print("")

#function that will output the names of unhealthy checks
def print_Names(given_json):
  for item in given_json["Checks"]:
    status = item.get("Status")
    if status == "unHealthy":
        name = item.get("Name")
        print(f"Name: {name}")



print(count_Status(given_json))
print(print_Names(given_json))

print(given_json["Checks"][0]["Status"])


# def countChecks(given_json):
#     for x in given_json:
# if 'Healthy' in given_json:    
#     print("yes")

# print(countChecks(given_json))


