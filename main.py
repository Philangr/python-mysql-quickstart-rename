from db_utils import create_connection, execute_query

mydb = create_connection("localhost", "root", "your_mysql_root_password", "my_sandbox_db")  # CHANGE PASSWORD HERE

if mydb:
    print("Successfully connected to the database!")
    mydb.close()

# TODO: run the setup_db script to initialize the database.
