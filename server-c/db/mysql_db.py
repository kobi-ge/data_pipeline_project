import mysql.connector
from mysql.connector import pooling
import os 


class MySQLManager():
    def __init__(self,url:str):
        self.pool = pooling.MySQLConnectionPool(
            pool_name='mypool'
            pool_size=5
            host=DATABASE_HOST
        )