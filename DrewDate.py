import json

# User inputs their budget
# Return "Welcome <user>! You're going on a date with <users_date>. You will be eating at $$$"

user_name = input("Please enter your name: ")
user_date_name = input("Please enter your dates name: ")
user_budget = float(input("Please enter you budget: $"))


# Output the welcome message and budget
print(f"\nWelcome {user_name}! You are going on a date with {user_date_name}! You will be eating at Olive Garden\n")
print(f"Your budget is ${user_budget}. Good luck!\n")
# Define the food menus


menu = {
  "Main":{
    "steak": 30.00,
    "spaghetti": 45.00,
    "salad": 20.00
  }
}

def user_order(menu, budget):
    order_total = 0.00

    for category, item in menu.items():
      user_entre = float(input(f"Please select your entree amount {item} "))
      order_total = user_entre * 2
      budget = budget - order_total

      print(f"The total for you and {user_date_name} is ${order_total}")
    
    if order_total < budget:
      print(f"{user_name}. You will have a second Date :)")
    else:
      print(f"{user_name}. You will not have a second Date :(")


user_order(menu, user_budget)
    
