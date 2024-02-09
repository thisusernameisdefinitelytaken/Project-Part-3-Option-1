# Course Project Part 2: Python Program
# Option 1: Business Python Program
# Name: Celeste Hernandez Mora
# Date: 8 February 2024
# Purpose: To appoint a time for the delivery of goods, with the user choosing the goods and the appointment

# import custom module
import shopping

# simple function to execute 'shop' commands
def executeShop(shop):
  shop.displayMenu()
  shop.addItem()

# simple function to execute 'deliver' commands
def executeDeliver(deliver):
  deliver.displayMenu()
  choice = deliver.selection()
  return choice # get user's selection

# introduction to goods
print("\t\t\t\t*** Daily Discounts ***")
print("\nWelcome! For each day, five randomly-picked items receive a significant discount.")
print("\nThe items of the day are as follows:")

# declare variables for holding goods
purchases = []
sale = {1: ("Air Fryer", 70.99), 2: ("Smart TV", 199.99), 3: ("Kitchenware Set", 80.49), 4: ("Couch", 248.99), 5: ("Washing Machine", 279.99), 6: ("EXIT", 0.00)}

# conduct the entire process for selecting goods
shop = shopping.PurchaseItem(sale, purchases)
executeShop(shop)

# ask for a delivery date, declare variable holding six possible appointments
print("\nPlease select an available date to deliver the goods:")
dates = {1: ("2:00 PM", "February 9th"), 2: ("8:00 PM", "February 9th"), 3: ("11:00 AM", "February 10th"), 4: ("2:00 PM", "February 10th"), 5: ("6:00 PM", "February 12th"), 6: ("8:00 PM", "February 12th")}

# conduct the entire process for selecting a delivery date
deliver = shopping.DeliverItem(dates)
choice = executeDeliver(deliver)

# print the user's selection, both into a text file and out of that text file
show = shopping.InfoPrint(sale, purchases, dates, choice)
show.combine()