import fileinput
# Feedback (Salma Maikano) from previous submission suggested I made it more user-friendly.
# I tabulated the view_all function to rectify this (improvement from previous submission).
from tabulate import tabulate


# ========The beginning of the class==========

class Shoes:  # Define parent class as shoe

    def __init__(self, country, code, product, cost, quantity):  # Constructor to make instance variables
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_code(self):
        return self.code

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()


# ================== FUNCTIONS ==================== #
# Create variable to open inventory.txt file and use read modifier
invent_read = open("inventory.txt", "r")

items_list = []  # First list for shoe items read from file
shoe_obj_list = []  # Second list for shoe objects transferred from items_list


# Define function to Read shoe data from inventory.txt
def read_shoes_data():
    file = None
    try:  # try/except/finally block for defensive programming. Incase the file is not found.
        header_line = invent_read.readline()  # Store header of text file into variable
        for lines in invent_read:
            strip_lines = lines.strip("\n")
            split_lines = strip_lines.split(",")
            items_list.append(split_lines)  # Append shoe items to empty items_list

        for i in range(0, len(items_list)):
            array = items_list[i]
            shoe1 = Shoes(array[0], array[1], array[2], array[3], int(array[4]))
            shoe_obj_list.append(shoe1)  # Cast each item into an object then append to new shoe_obj_list.

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            fileinput.close()
        return header_line


# Extract data on shoe and use data to create shoe object and append to shoe_object_list
def capture_shoes():
    c_country = input("Enter name of country shoe is from:\n")
    c_code = input("Enter the code of your shoe:\n")
    c_product = input("Enter the name of your shoe:\n")
    c_cost = int(input("Enter the cost of your shoe, only in numbers. e.g. 12345\n"))
    c_quantity = int(input("Enter the quantity of your product, only in numbers. E.g. 2\n"))

    capt_shoe = Shoes(c_country, c_code, c_product, c_cost, c_quantity)
    shoe_obj_list.append(capt_shoe)
    print("Shoe data has been captured and sent to list")


# Define function that will iterate over the shoe_list and print details.
# Use tabulate function to present data in a use-friendly manner(improvement from previous submission).
def view_all():
    file = None

    try:

        print("\nSTOCK LIST")

        country = []
        code = []
        product = []
        cost = []
        table = []
        quantity = []
        # For loop t iterate over each shoe and get data
        for i in range(len(shoe_obj_list)):
            country.append(shoe_obj_list[i].country)
            code.append(shoe_obj_list[i].code)
            product.append(shoe_obj_list[i].product)
            cost.append(shoe_obj_list[i].cost)
            quantity.append(shoe_obj_list[i].quantity)

        table = zip(country, code, product, cost, quantity)
        # Print tabulate to make it user-friendly and readable (improvement from previous submission)
        print(tabulate(table, headers=('Country', 'Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid'))

    except FileNotFoundError as error:
        print("\nError! This file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            fileinput.close()


#  Define function to find shoe of lowest quantity to re-stock
def re_stock():
    lowest_quantity = shoe_obj_list[0]
    for shoe in shoe_obj_list:  # Iterate over shoe list to get lowest quantity
        if shoe.get_quantity() < lowest_quantity.get_quantity():
            lowest_quantity = shoe
    print("Least amount of stock details:\n" + str(lowest_quantity))
    # Ask if user wants to restock
    restock_opt = input("Do you want to restock shoes? yes/no: ").lower()
    if restock_opt == "yes":
        quant_update = int(input("Please enter the new quantity to update: "))
        lowest_quantity.quantity = quant_update
        print(f"Stock quantity of this product has been updated to: {lowest_quantity.quantity}")
    else:  # issue
        print("You do not wish to restock.")


# Define function to use shoe code to find shoe from list and print the shoe selected
def search_shoe():
    search_shoe = input("\nPlease enter the code you are searching for:\n\n").upper()

    for line in shoe_obj_list:
        if line.get_code() == search_shoe:  # Use get_code method to find shoe
            print(f'\n {line}')  # Print into output

    print("\nPlease select another option\n")


# Define function that will calculate the total value for each item.
def value_per_item():
    value = 0
    for shoe in shoe_obj_list:
        value = int(shoe.get_cost()) * shoe.get_quantity()  # Use get_cost and get_quantity method
        print(str(shoe) + "\tTotal Value: " + "ZAR", str(value))
    return value


# Define function that will get product with the highest quantity and print shoe for sale
def highest_quantity():
    highest_qty = []  # Create list containing highest quantity shoe

    for line in shoe_obj_list:
        highest_qty.append(line)  # For loop to find highest quantity shoe then append to list

    print("\n•••••Highest stock item:•••••\n")
    # Use key=lambda to sort through and print max quantity.
    # Learned about key=lambda ref below:
    # https://stackoverflow.com/questions/13669252/what-is-lambda-in-python-code-how-does-it-work-with-key-arguments-to-sorte
    print(max(shoe_obj_list, key=lambda item: item.quantity))
    print("\nThis item has now been marked on sale\n")
    print("\nPlease select another option")


# Define function to update inventory text file after re-stock and capture
def update_inventory():
    with open('inventory.txt', 'w') as f:
        f.write(header)  # Write header into inventory file
        for i in range(len(shoe_obj_list)):
            task_info = (f"{shoe_obj_list[i].country},{shoe_obj_list[i].code},{shoe_obj_list[i].product}," +
                         f"{shoe_obj_list[i].cost},{shoe_obj_list[i].quantity}\n")
            f.write(task_info)  # Write task info into inventory file


# ==========Main Menu=============


# Display menu options using while True.
# Call read_shoes_data method so all shoes from items list are cast to object and appended to shoe_object_list.
# Use try/except block for value error - Defensive Programming
header = read_shoes_data()  # Create header variable so when we write over inventory, headers are still there.
while True:

    try:
        menu = int(input('''\n 
            To select choice enter number assigned to task:
            1. Capture Shoes
            2. View All
            3. Restock Shoe
            4. Search Shoe
            5. View Item Values
            6. View Sale Item
            0. Exit and save changes
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            view_all()
            re_stock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_quantity()

        elif menu == 0:
            update_inventory()
            exit()
        else:
            print("\nYou have selected an invalid option. Please try again by choosing from the menu below.\n")

    except ValueError:
        print("\nYou have selected an invalid option. Please try again by entering a number.\n")
