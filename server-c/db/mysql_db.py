import mysql.connector
import os 

DATABASE_HOST = os.getenv("DATABASE_HOST","host")
DATABASE_USER = os.getenv("DATABASE_USER","user")
DATABASE_PASSWORD = os.getenv("DATABASE_HOST","pass")
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

db_manager = MySQLManager(host=DATABASE_HOST,user=DATABASE_USER,password=DATABASE_PASSWORD,database_name=DATABASE_NAME)