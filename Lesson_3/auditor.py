inventory = 0
fail = 0
stock = 0


def get_valid_input():
    global fail
    global stock

    if stock.isdigit():
        print("Pass")
        return stock
    else:
        if stock != "quit":
            print("Invalid input. Please enter a positive number or 'quit' to exit.")
            fail = fail + 1
            stock = 0
        else:
            stock = "quit"
        return stock

def process_delivery(current_total, new_value):
    global fail
    global stock

    if current_total + new_value <= 500:
        current_total = current_total + new_value
        print("pass:", current_total)
        return current_total
    else:
        print("Inventory limit exceeded. Cannot add more stock.")
        fail += 1
        stock = "quit"
    return current_total

def calculate_tax(amount):
    tax_rate = 0.10
    tax_amount = amount * tax_rate
    return tax_amount

def generate_report(total_units, failed_attempts):
    print("Total Unit Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

while (stock != "quit"):
    stock = input("Enter stock quantity: ")
    if stock == "quit":
        break
    get_valid_input()
    inventory = process_delivery(int(inventory), int(stock))

generate_report(inventory, fail)


#Eugene Repo URL: https://github.com/Eugene2603188/Lab2

