import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model import Product, Warehouse, Inventory

engine = create_engine('sqlite:///inventory.db')
Base = declarative_base()

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
def view_inventory():
    inventory = session.query(Inventory).all()
    for item in inventory:
        product = session.query(Product).filter_by(id=item.product_id).first()
        warehouse = session.query(Warehouse).filter_by(id=item.warehouse_id).first()
        click.echo(f'Product ID: {item.product_id}, Warehouse: {warehouse.name}, Quantity: {item.quantity}')

@cli.command()
@click.option('--name', prompt='Product name', help='Name of the product')
@click.option('--description', prompt='Product description', help='Description of the product')
@click.option('--price', prompt='Product price', help='Price of the product')
def add_product(name, description, price):
    product = Product(name=name, description=description, price=price)
    session.add(product)
    session.commit()
    click.echo(f'Product {name} added successfully')

@cli.command()
@click.option('--name', prompt='Warehouse name', help='Name of the warehouse')
@click.option('--address', prompt='Warehouse address', help='Address of the warehouse')
def add_warehouse(name, address):
    warehouse = Warehouse(name=name, address=address)
    session.add(warehouse)
    session.commit()
    click.echo(f'Warehouse {name} added successfully')

if __name__ == "__main__":
    cli()