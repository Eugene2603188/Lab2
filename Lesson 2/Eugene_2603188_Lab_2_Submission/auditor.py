inventory = 0
fail = 0

stock = input("Enter stock quantity: ")

while (stock != "quit"):
    if stock.isdigit():
        if ((int(inventory) + int(stock)) > 500):
            print("Inventory limit exceeded. Cannot add more stock.")
            fail += 1
            stock = "quit"
        else:
            inventory += int(stock)
            print("Current Inventory:", inventory)
            stock = input("Enter stock quantity: ")
    else:
        print("Invalid input. Please enter a positive number or 'quit' to exit.")
        #is.digit() alrdy checks for positive numbers and negative numbers mah

        fail += 1
        stock = input("Enter stock quantity: ")
print("Total Unit Processed:", inventory)
print("Number of Failed/Rejected Entries:", fail)

#Eugene Repo URL: https://github.com/Eugene2603188/Lab2

