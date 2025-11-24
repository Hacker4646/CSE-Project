# Bakery Items CRUD Application

bakery_items = []   # List to store bakery item records

def add_item():
    print("\n--- Add Bakery Item ---")
    item_id = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    price = float(input("Enter Item Price: "))

    bakery_items.append({
        "id": item_id,
        "name": name,
        "price": price
    })
    print("Item added successfully!")

def view_items():
    print("\n--- Bakery Items List ---")
    if len(bakery_items) == 0:
        print("No items found.")
    else:
        for item in bakery_items:
            print(f"ID: {item['id']} | Name: {item['name']} | Price: {item['price']}")

def update_item():
    print("\n--- Update Bakery Item ---")
    item_id = input("Enter Item ID to update: ")

    for item in bakery_items:
        if item["id"] == item_id:
            item["name"] = input("Enter New Name: ")
            item["price"] = float(input("Enter New Price: "))
            print("Item updated successfully!")
            return
    
    print("Item not found!")

def delete_item():
    print("\n--- Delete Bakery Item ---")
    item_id = input("Enter Item ID to delete: ")

    for item in bakery_items:
        if item["id"] == item_id:
            bakery_items.remove(item)
            print("Item deleted successfully!")
            return

    print("Item not found!")

def menu():
    while True:
        print("\n===== BAKERY MANAGEMENT SYSTEM =====")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the Program
menu()
