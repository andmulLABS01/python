# ansFist = input('Please enter your First name? ')
# ansLast = input('Please enter your Last name? ')

# if ansLast == '':
#   ans = input("Would you like to submit without entering your last name? Type Yes or No Do you like Pets, yes or no? ")

# if ans.lower() == 'no' or ans.lower() == 'n':
#     exit
# elif ans.lower() == 'yes' or ans.lower() == 'y':
#     print("Thank you the form was submitted")
# else:
#     print("Thank you the form was submitted")


# #   print("You do not like pets. Are you sure? ")
# #   ans = input("Do you like Pets, yes or no? ")

import subprocess

# List of IP addresses to ping
ip_addresses = [
    "54.234.140.138",
    "3.81.114.140",
    "3.81.215.202",
]

# Function to ping an IP address and check if it's reachable
def ping_ip(ip):
    try:
        subprocess.check_output(["ping", "-c", "1", ip])
        return True
    except subprocess.CalledProcessError:
        return False

# Loop through the list of IP addresses and ping each one
for ip in ip_addresses:
    if ping_ip(ip):
        print(f"{ip} is reachable.")
    else:
        print(f"{ip} is not reachable.")

