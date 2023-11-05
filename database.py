from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Product, Warehouse, Inventory

engine = create_engine('sqlite:///inventory.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, description, price, warehouse):
    product = Product(name=name, description=description, price=price)
    session.add(product)
    session.commit()
    inventory = Inventory(product_id=product.id, warehouse_id=warehouse.id, quantity=0)
    session.add(inventory)
    session.commit()

def delete_product(product_id):
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        session.delete(product)
        session.commit()

def delete_inventory(inventory_id):
       inventory = session.query(Inventory).filter_by(id=inventory_id).first()
       if inventory:
           session.delete(inventory)
           session.commit()

def delete_warehouse(warehouse_id):
    warehouse = session.query(Warehouse).filter_by(id=warehouse_id).first()
    if warehouse:
        session.delete(warehouse)
        session.commit()
def get_product_by_id(product_id):
    return session.query(Product).filter_by(id=product_id).first()

def add_warehouse(name, address):
    warehouse = Warehouse(name=name, address=address)
    session.add(warehouse)
    session.commit()

def get_warehouse_by_id(warehouse_id):
    return session.query(Warehouse).filter_by(id=warehouse_id).first()

def add_inventory(product_id, warehouse_id, quantity):
    inventory = Inventory(product_id=product_id, warehouse_id=warehouse_id, quantity=quantity)
    session.add(inventory)
    session.commit()

def get_inventory_by_product_and_warehouse(product_id, warehouse_id):
    return session.query(Inventory).filter_by(product_id=product_id, warehouse_id=warehouse_id).first()

def get_warehouse_by_address(address):
    return session.query(Warehouse).filter_by(address=address).first()