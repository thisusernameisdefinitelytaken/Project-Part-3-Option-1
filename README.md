# Project-Part-3-Option-1
Program is for Option 1: Business Python Program. \
CIS-30A-21273\
PURPOSE AND FUNCTION:\
The purpose of this program is to imagine a business transaction in which the user selects items from the menu to purchase, as many as they wish until they choose to stop or until the error is activated through invalid input. The user may then choose an appointed time and day in which their goods can be delivered, with the dates being given through another menu. 
Once the user's selections are in, the program will create a text file in which the selections are recorded in. Items purchased, their total, and appointed date are all written into a new text file called "purchase.txt". Once the information is recorded in, the information will then be drawn out of purchase.txt and read to the user via output.\
STRUCTURE:\
The program consists of two modules: 'main.py' and 'shopping.py'. The module, shopping.py, is to be imported into main.py.
The primary module, main.py, consists of two functions: executeShop and executeDeliver. The former executes two main functions for purchasing goods, which outputs the menu for goods and records new purchases. The latter executes two main functions for delivering goods, including one that displays the menu and another that gets the user's selection.\
The imported module, shopping.py, consists of three classes: PurchaseItem, DeliverItem, and InfoPrint. Each have their own collection of functions, but different purposes as their names imply. The program consists of three parts, and these three classes serve each part respectively. PurchaseItem does the section where the user is selecting and purchasing goods. DeliverItem is for choosing a delivery date for the purchasing goods to arrive in. Finally, InfoPrint is responsible for creating and reading the text file 'purchase.txt', which contains the purchases and appointed time as chosen by the user.\
EXTRA:\
There is an additional text file titled 'extra file - output of program'. This is merely the output of one of my runs of this program, just so a demonstration can be quickly accessed.\
