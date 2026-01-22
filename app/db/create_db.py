from sqlalchemy import text,create_engine
from dotenv import load_dotenv
import os

load_dotenv()

database_url=os.getenv("db_url")

engine=create_engine(database_url)

db_name="dayflow"

def create_db():
    with engine.connect() as conn:
        conn.execute(text(f'CREATE DATABASE IF NOT EXISTS {db_name}'))
        print(f'Database Created Successfully {db_name}')

if __name__ == "__main__":
    create_db()