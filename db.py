# this file lets you create a connection to mysql, and execute a query against mysql

import mysql.connector

def create_connection():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="things"
        )
        return db_connection
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

# TODO: Should we have a separate method for executing queries and queries that return results?
def execute_query(db_connection, query):
    if db_connection:
      mycursor = db_connection.cursor(buffered=True)
      try:
          # do the thing that the query says
          mycursor.execute(query)

          # commit it, making it take effect
          db_connection.commit()

          # did the query return data? Send to the caller!
          return mycursor.fetchall()
      except mysql.connector.Error as err:
          print(f"Query execution failed: {err}")
          # it didn't work, rollback the query
          db_connection.rollback()
          return None
    return None
