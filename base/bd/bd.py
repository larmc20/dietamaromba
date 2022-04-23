#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Módulo de funções banco de dados
"""
from psycopg2 import connect

class database:

    """Database class
    """
    def __init__(self):
        pass
    
    def connect_db(self):
                
        # Connect to your postgres DB
        conn = connect(dbname='dieta', user='postgres', host='localhost', port = '5432', password='Tui12312@')

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a query
        #cur.execute("SELECT * FROM my_data")

        # Retrieve query results
        #records = cur.fetchall()

        print(conn)
    



o = database()
o.connect_db()
