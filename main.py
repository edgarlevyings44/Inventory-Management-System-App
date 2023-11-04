from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Warehouse, Inventory, Product
from database import (
    add_product,
    get_product_by_id,
    get_warehouse_by_id,
    add_inventory,
    add_warehouse,
    delete_product,
    delete_warehouse,
    delete_inventory,
)

def add_new_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    warehouse_name = input("Enter warehouse name: ")
    warehouse_address = input("Enter warehouse address: ")
    warehouse = add_warehouse(warehouse_name, warehouse_address)
    add_product(name, description, price, warehouse)
    print("Product added successfully!")

def update_product():
    product_id = int(input("Enter product ID: "))
    product = get_product_by_id(product_id)
    if product:
        print("Product found!")
        name = input("Enter updated product name: ")
        description = input("Enter updated product description: ")
        price = float(input("Enter updated product price: "))
        product.name = name
        product.description = description
        product.price = price
        session.commit()
        print("Product updated successfully!")
    else:
        print("Product not found!")

def delete_product_by_id():
    product_id = int(input("Enter product ID: "))
    delete_product(product_id)
    print("Product deleted successfully!")

def delete_warehouse_by_id():
    warehouse_id = int(input("Enter warehouse ID: "))
    delete_warehouse(warehouse_id)
    print("Warehouse deleted successfully!")

def delete_inventory_by_ids():
    product_id = int(input("Enter product ID: "))
    warehouse_id = int(input("Enter warehouse ID: "))
    delete_inventory(product_id, warehouse_id)
    print("Inventory deleted successfully!")

def add_inventory():
    product_id = int(input("Enter product ID: "))
    warehouse_id = int(input("Enter warehouse ID: "))
    quantity = int(input("Enter quantity: "))
    add_inventory(product_id, warehouse_id, quantity)
    print("Inventory added successfully!")

def add_new_warehouse():
    name = input("Enter warehouse name: ")
    address = input("Enter warehouse address: ")
    add_warehouse(name, address)
    print("Warehouse added successfully!")

def main():
    engine = create_engine('sqlite:///inventory.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add New Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Delete Warehouse")
        print("5. Add Inventory")
        print("6. Add Warehouse")
        print("7. Delete Inventory")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            add_new_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            delete_product_by_id()
        elif choice == "4":
            delete_warehouse_by_id()
        elif choice == "5":
            add_inventory()
        elif choice == "6":
            add_new_warehouse()
        elif choice == "7":
            delete_inventory_by_ids()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()