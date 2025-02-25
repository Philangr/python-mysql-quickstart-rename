# this file lets you create a connection to mysql, and execute a query against mysql

import mysql.connector

def create_connection():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password here",
            database="things"
        )
        return mydb
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

# TODO: Should we have a separate method for executing queries and queries that return results?
def execute_query(mydb, query):
    if mydb:
      mycursor = mydb.cursor()
      try:
          mycursor.execute(query)
          mydb.commit()
          return mycursor.fetchall()
      except mysql.connector.Error as err:
          print(f"Query execution failed: {err}")
          mydb.rollback()
          return None
    return None
