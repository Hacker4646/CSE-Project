A simple Python console-based application that allows a bakery to manage its products using basic CRUD operations:

C → Create (Add new bakery items)

R → Read (View all items)

U → Update (Modify item details)

D → Delete (Remove items)

This program uses a list of dictionaries to store bakery items and provides a user-friendly menu system.

 Features

  Add new bakery items
  View list of all items
  Update existing items
  Delete items by ID
  Easy text-based menu interface

 Technologies Used

Python 3.x

Standard input/output (No external libraries required)

How to Run

Install Python 3.x on your computer.

Copy the program into a file named:

bakery_crud.py


Open terminal/command prompt and run:

python bakery_crud.py


Use the menu to interact with the application.

 Program Overview

The application contains the following main functions:

Function	Description
add_item()	Adds a new bakery item with ID, name, and price
view_items()	Displays all items stored
update_item()	Updates item details based on ID
delete_item()	Deletes item by ID
menu()	Shows user menu and takes input

All items are stored in a list of dictionaries:

bakery_items = [
    {
        "id": "101",
        "name": "Bread",
        "price": 25.0
    }
]

Sample Menu Output
===== BAKERY MANAGEMENT SYSTEM =====
1. Add Item
2. View Items
3. Update Item
4. Delete Item
5. Exit
Enter your choice:

Example Use Case

Bakery manager enters new products

Can edit price when cost changes

Can view available items

Can delete discontinued bakery items

 Future Enhancements

 Store records in a text/JSON file
    Add database support
  Create a GUI using Tkinter
  Add search feature by name or price
