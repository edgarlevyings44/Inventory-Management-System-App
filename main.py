from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Warehouse, Inventory
from database import add_product, get_product_by_id, get_warehouse_by_id, add_inventory

def add_new_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    add_product(name, description, price)
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

def delete_product():
    product_id = int(input("Enter product ID: "))
    product = get_product_by_id(product_id)
    if product:
        print("Product found!")
        session.delete(product)
        session.commit()
        print("Product deleted successfully!")
    else:
        print("Product not found!")

def d_warehouse(warehouse_id):
    warehouse = get_warehouse_by_id(warehouse_id)
    if warehouse:
        session.delete(warehouse)
        session.commit()
        print("Warehouse deleted successfully!")
    else:
        print("Warehouse not found!")

def get_warehouse_by_id(warehouse_id):
    return session.query(Warehouse).filter_by(id=warehouse_id).first()

def add_inventory(product_id, warehouse_id, quantity):
    inventory = Inventory(product_id=product_id, warehouse_id=warehouse_id, quantity=quantity)
    session.add(inventory)
    session.commit()
    print("Inventory added successfully!")

def main():
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add New Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Delete Warehouse")
        print("5. Add Inventory")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_new_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            warehouse_id = int(input("Enter warehouse ID: "))
            d_warehouse(warehouse_id)
        elif choice == "5":
            product_id = int(input("Enter product ID: "))
            warehouse_id = int(input("Enter warehouse ID: "))
            quantity = int(input("Enter quantity: "))
            add_inventory(product_id, warehouse_id, quantity)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    engine = create_engine('sqlite:///inventory.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    main()