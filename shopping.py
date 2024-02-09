# class to purchase items
class PurchaseItem:
  # get sale and purchases from main
  def __init__(self, sale, purchases):
    self.sale = sale
    self.purchases = purchases

  # display menu of goods
  def displayMenu(self):
    for j, k in self.sale.items():
      if j != 6:
        print(j, ":", k[0], "for $", k[1])
      else:
        print(j, ":", k[0])

  # continuosly add goods as requested by user
  def addItem(self):
    # declare variables
    total = 0.00
    choice = 0
    # loop until choice = 6
    while (choice != 6):
      # assertion; continue until choice is 6, or error if choice is not within 1-6
      try:
        choice = int(input("\nPlease enter your selection: "))
        assert choice <= 6
      except AssertionError:
        print("Invalid selection.")
      else:
        if choice != 6:
          print("You have added", self.sale[choice][0], "to your cart.")
        else:
          print("You have chosen to exit.")
          break

      # add new item to total purchases
      self.purchases.append(self.sale[choice])
      self.currentCart(total)
      total = 0.00

  # print selected goods thus far
  def currentCart(self, total):
    print("Your shopping cart:")
    for m in self.purchases:
      print(m[0], " $", m[1])
      total += m[1]
    print("Total: ${:0.2f}". format(total))

# class to deliver the goods
class DeliverItem:
  # get dates from main
  def __init__(self, dates):
    self.dates = dates

  # display available delivery dates
  def displayMenu(self):
    for o, p in self.dates.items():
      print(o, ":", p[1], "at", p[0])

  # get user's selection, make sure it is within 1-6
  def selection(self):
    try:
      choice2 = int(input("\nPlease enter your selection: "))
      assert choice2 <= 6
    except AssertionError:
      print("Invalid selection.")
    else:
      print("You have chosen the delivery date of:", self.dates[choice2][1], "at", self.dates[choice2][0], ".")
      return choice2 # return choice

# child class of PurchaseItem
# creates a text file of the user's selections,
# then outputs the file's contents to the user
class InfoPrint(PurchaseItem):
  # inhert from PurchaseItem, get variables from main
  def __init__(self, sale, purchases, dates, choice):
    PurchaseItem.__init__(self, sale, purchases)
    self.dates = dates
    self.choice = choice

  # create text file
  def display(self):
    with open("purchase.txt", "w") as f:
      f.write("\n\t *** Your Purchases ***")
      f.write("\n-----------------------------------\n")

  # append in the chosen goods
  def displayItems(self):
    with open("purchase.txt", "a") as f:
      for j in self.purchases:
        f.write("{} . . . ${:0.2f}\n". format(j[0].upper(), j[1]))

  # append in the total
  def displayTotal(self):
    total = 0.00
    for k in self.purchases:
      total += k[1]
      
    with open("purchase.txt", "a") as f:
      f.write("-----------------------------------")
      f.write("\nTOTAL: \t\t\t ${:0.2f}". format(total))

  # append in the appointed date
  def displayDate(self):
    with open("purchase.txt", "a") as f:
      f.write("\nEXPECTED: \t\t" + self.dates[self.choice][1] + " at " + self.dates[self.choice][0])

  # call all functions above to create text file,
  # then read it at the end
  def combine(self):
    self.display()
    self.displayItems()
    self.displayTotal()
    self.displayDate()

    with open("purchase.txt", "r") as f:
      for line in f:
        print(line)