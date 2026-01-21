import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract
import os 

DATABASE_HOST = os.getenv("DATABASE_HOST","localhost")
DATABASE_USER = os.getenv("DATABASE_USER","root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD","pass")
DATABASE_NAME = os.getenv("DATABASE_NAME","sql_db")


class MySQLManager():
    def __init__(self,host:str,user:str,password:str,database_name:str):

        self.pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name='mypool',
            pool_size=5,
            host=host,
            user=user,
            password=password,
            database=database_name
        )
    def get_db(self):
        connection = self.pool.get_connection()
        try:
            yield connection
        finally:
            connection.close()
    
    def init_schema(self):
        
        table_name = os.getenv('TABLE_NAME','records_table')
        
        conn : MySQLConnectionAbstract = self.pool.get_connection()
        
        try:
            cursor : MySQLCursorAbstract = conn.cursor()
            query: str = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    timestamp DATETIME,
                    location_name VARCHAR,
                    country VARCHAR,
                    latitude FLOAT,
                    longitude FLOAT,
                    temoerature FLOAT,
                    wind_speed FLOAT,
                    humidity INT,
                    temperature_category VARCHAR(100),
                    wind_category VARCHAR(100)
                )
            """
            cursor.execute(query)
            conn.commit()
            cursor.close()
            
        finally:
            conn.close()
                

db_manager = MySQLManager(host=DATABASE_HOST,user=DATABASE_USER,password=DATABASE_PASSWORD,database_name=DATABASE_NAME)