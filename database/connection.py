import mysql.connector

def DatabaseConnection():
    try:
        db_config=mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql',
            database='psm'
        )
        return db_config
    except Exception as e:
        return f"something went wrong in connecion : {e}"