import click
from sqlalchemy.orm import sessionmaker
from database import engine, Base, Product, Warehouse, Inventory

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

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
def view_inventory():
    inventory = session.query(Inventory).all()
    for item in inventory:
        product = session.query(Product).filter_by(id=item.product_id).first()
        warehouse = session.query(Warehouse).filter_by(id=item.warehouse_id).first()
        click.echo(f'Product ID: {item.product_id}, Warehouse: {warehouse.name}, Quantity: {item.quantity}')

if __name__ == '__main__':
    cli()