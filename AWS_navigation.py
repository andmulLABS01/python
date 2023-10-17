import json


givenJSON = """
{
    "Reservations": [
        {
            "ReservationId": "r-0b9d09c7fbb123456",
            "Instances": [
                {
                    "InstanceId": "i-0123456789abcdef0",
                    "InstanceType": "t2.micro",
                    "KeyName": "my-key-pair",
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "PrivateIpAddress": "172.31.16.150",
                    "PublicIpAddress": "52.14.82.122",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "web-server-1"
                        },
                        {
                            "Key": "environment",
                            "Value": "dev"
                        }
                    ],
                    "SecurityGroups": [
                        {
                            "GroupName": "my-security-group",
                            "GroupId": "sg-0123456789abcdef0"
                        }
                    ],
                    "SubnetId": "subnet-0123456789abcdef0",
                    "VpcId": "vpc-0123456789abcdef0"
                },
                {
                    "InstanceId": "i-0123456789abcdef1",
                    "InstanceType": "t2.micro",
                    "KeyName": "my-key-pair",
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "PrivateIpAddress": "172.31.16.151",
                    "PublicIpAddress": "54.14.82.123",
                    "State": {
                        "Code": 16,
                        "Name": "disabled"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "web-server-2"
                        },
                        {
                            "Key": "environment",
                            "Value": "stg"
                        }
                    ],
                    "SecurityGroups": [
                        {
                            "GroupName": "my-security-group",
                            "GroupId": "sg-0123456789abcdef0"
                        }
                    ],
                    "SubnetId": "subnet-0123456789abcdef0",
                    "VpcId": "vpc-0123456789abcdef0"
                },
                {
                    "InstanceId": "i-0123456789abcdef2",
                    "InstanceType": "t2.micro",
                    "KeyName": "my-key-pair",
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "PrivateIpAddress": "172.31.16.152",
                    "PublicIpAddress": "52.14.82.124",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "web-server-3"
                        },
                        {
                            "Key": "environment",
                            "Value": "dev"
                        }
                    ],
                    "SecurityGroups": [
                        {
                            "GroupName": "my-security-group",
                            "GroupId": "sg-0123456789abcdef0"
                        }
                    ],
                    "SubnetId": "subnet-0123456789abcdef0",
                    "VpcId": "vpc-0123456789abcdef0"
                }
            ]
        }
    ]
}
"""
# In One Function, Print the following questions/answers each on a new line:

# 1: The total number of instance ID's in input_json
# 2: The instance ID's where state is running
# 3: The instance ID's tagged with env stg, get the ip address of stg instance

#format your JSON String to load like json
instance_json = json.loads(givenJSON)


#One Function, Print the questions/answers each on a new line:
def Q_A(instance_json):
# Count total number of instance ID's in input_json
  count_instanceID = 0

# Go through the dictionary and count using a for loop with if elif statements
  for item in instance_json["Reservations"]:
    id = item.get("Instances")
    for x in id:
        ID = x.get("InstanceId")
        if ID != "":
            count_instanceID += 1

  print("1: The total number of instance ID's in input_json")
  print(count_instanceID,)








print(Q_A(instance_json))