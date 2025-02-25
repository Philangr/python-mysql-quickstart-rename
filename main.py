from db import create_connection, execute_query

mydb = create_connection()

if mydb:
    print("Successfully connected to the database!")

    print(execute_query("SELECT * FROM thing;"))
    
    mydb.close()

# TODO: run the setup_db script to initialize the database.
