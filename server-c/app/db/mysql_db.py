import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract
import os 
import time

DATABASE_HOST = os.getenv("DATABASE_HOST","127.0.0.1")
DATABASE_USER = os.getenv("DATABASE_USER","root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD","")
DATABASE_NAME = os.getenv("DATABASE_NAME","sql_db")
DATABASE_PORT = int(os.getenv("DATABASE_PORT","3306"))
TABLE_NAME = os.getenv('TABLE_NAME','records_table')


class MySQLManager():
    def __init__(self,host:str,user:str,password:str,port:int):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.pool = None 
        
    def initialize_pool(self):
        retries = 5 
        for i in range(retries):
            try:
                self.pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name = 'my-pool',
            pool_size = 5,
            host = self.host,
            user = self.user,
            password = self.password,
            port = self.port
        )
            except mysql.connector.Error as err:
                print(f'connection failed {err}. retry again {i}')
                time.sleep(3)
        raise Exception("connection failed after all retries")

    def get_db(self):
        if not self.pool:
            raise Exception("Database pool not initialized. Call initialize_pool() first.")
        connection = self.pool.get_connection()
        try:
            yield connection
        finally:
            connection.close()
    def init_database(self):
        conn : MySQLConnectionAbstract= self.pool.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")
            
            conn.commit()
            cursor.close()
        finally:
            cursor.close()
            conn.close()
    def init_schema(self):
        conn : MySQLConnectionAbstract = self.pool.get_connection()
        try:
            cursor : MySQLCursorAbstract = conn.cursor()
            cursor.execute(f"USE {DATABASE_NAME}")
            query: str = f"""
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    timestamp DATETIME,
                    location_name VARCHAR(100),
                    country VARCHAR(100),
                    latitude FLOAT,
                    longitude FLOAT,
                    temperature FLOAT,
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
            cursor.close()
            conn.close()
                

db_manager = MySQLManager(host=DATABASE_HOST,user=DATABASE_USER,password=DATABASE_PASSWORD,port=DATABASE_PORT)