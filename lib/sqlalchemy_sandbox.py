from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an engine (SQLite in this case)
engine = create_engine('sqlite:///example.db', echo=True)

# Define a base class for the declarative system
Base = declarative_base()

# Define a class representing a table
class User(Base):
    __tablename__ = 'users'

    # Define columns for the 'users' table
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String(50), nullable=False)  # String column with max length 50
    age = Column(Integer, nullable=False)  # Integer column



# Create the tables in the database
Base.metadata.create_all(engine)
