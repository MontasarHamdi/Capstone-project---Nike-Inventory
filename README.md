CAPSTONE PROJECT IV

NIKE SHOE INVENTORY MANAGER

The main aim of the project was to create a Python program that will read from the text file inventory.txt and perform 
the following on the data, to prepare for presentation to your managers:

▪ read_shoes_data - This function will open the file inventory.txt and read the data from this file, then create a shoes
object with this data and append this object into the shoes list. 

▪ capture_shoes - This function will allow a user to capture data about a shoe and use this data to create a shoe object
and append this object inside the shoe list.

▪ view_all - This function will iterate over the shoes list and print the details of the shoes returned from the __str__
function. I used the tabulate module to present data output in table format.

▪ re_stock - This function will find the shoe object with the lowest quantity, which is the shoes that need to be 
re-stocked. Ask the user if they want to add this quantity of shoes and then update it. This quantity should be updated 
on the inventory.txt file for this shoe.

▪ search_shoe - This function will search for a shoe from the list using the shoe code and return this object so that it 
will be printed.

▪ value_per_item - This function will calculate the total value for each item. 

▪ highest_qty - Determine the product with the highest quantity and print this shoe as being for sale.

▪ update_inventory - When the user exits, all the changes made via restock and shoe capture will be updated onto the 
inventory.txt file.

* To use program make sure to have downloaded the inventory.txt file

