import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def DatabaseConnection():

    try:
        db_config = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT', 3306)
        )

        return db_config

    except Exception as e:
        return f"something went wrong in connection: {e}"