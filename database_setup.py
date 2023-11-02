from sqlalchemy import create_engine
from model import Base

# Create the database engine
engine = create_engine('sqlite:///inventory.db')

# Create the tables
Base.metadata.create_all(engine)

print("inventory.db created successfully with the necessary tables.")