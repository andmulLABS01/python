import json
import os
import csv

import sys
import subprocess

"""""
# Python Module OS - is used for file systems operations. Make and edit files. Use with env variables

# Python Module sys - runtime specfic features. Data that is needed during the time python file is running
  With this module we can chnage rules of how our python file runs

# Python Module subproccess to use python to run CLI commands with subprocesses

python addTags.py <instanceID> <tagKey> <tagValue>

"""
#i-010d9eb600f6c6e11

def addTags(instance_id, tag_key, tag_value):

  #Using subprocess to run aws cli command
  try:
    aws_command = f"aws ec2 create-tags --resources {instance_id} --tags Key={tag_key},Value={tag_value}"
    subprocess.run(aws_command, shell=True, check=True)
    print("subprocess ran successfully")
  except subprocess.CalledProcessError as e:
    print(f"Error Message: {str(e)}")


def main():
  #Checking for number of correct arguments
  if len(sys.argv) != 4:
    print("Usage: python addTags.py <instanceID> <tagKey>")
    sys.exit(1)

  #Now access command line arguments
  instance_id = sys.argv[1]
  tag_key = sys.argv[2]
  tag_value = sys.argv[3]
  
  #addTags function
  addTags(instance_id, tag_key, tag_value)

main()