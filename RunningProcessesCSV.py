#Import modules  os, psutil, and csv
import os
import psutil
import csv


# Test psutil to see what it returns using print() and print(type())
print(list(psutil.Process().as_dict().keys()))
print(type(list(psutil.Process().as_dict().keys())))

# Now we have the attributes and we learned that they are in a list.

# Looking up the values to the attribures, the follwoing attributes will give us the information we need to fill in our CSV file.
# 'pid', 'name', 'exe', 'cpu_percent','memory_info'
# psutil has a function called 'psutil.process_iter'.  This function returns an iterator yielding a Process class instance for all running processes on the local machine.
# This function also allows us to specify attributes, attrs=[], that we need for our output.  We now have enough information to proceeed. 


# Get a list of all running processes, defining an empty list
process_list = []

# Since the result of the 'psutil.process_iter' is a list we need to iterate thorugh it using a for loop
for p in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent', 'memory_info']):

    # We need to create a veraiable to plase the irritated data in and append the information to our empty list
    process_info = p.info
    process_list.append([
        process_info['pid'],
        process_info['name'],
        process_info['exe'],
        process_info['cpu_percent'],
        process_info['memory_info'].rss
    ])

# Define the CSV file name
P_csv_file = 'running_processes.csv'

# Write the process information to a CSV file
with open(P_csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Process ID #', 'Name', 'Executable Path', 'CPU Usage (%)', 'Memory Usage (bytes)'])
    writer.writerows(process_list)

print(f"Process information written to {P_csv_file}")
