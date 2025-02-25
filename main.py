from db import create_connection, execute_query

db_connection = create_connection()

if db_connection:
    print("Successfully connected to the database!")

    print(execute_query(db_connection, "SELECT * FROM thing;"))
    
    db_connection.close()

