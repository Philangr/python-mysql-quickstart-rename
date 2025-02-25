from db_utils import create_connection, execute_query

mydb = create_connection("localhost", "root", "your_mysql_root_password", "my_sandbox_db")  # CHANGE PASSWORD HERE

if mydb:
    print("Connected to the database!")

    # Example (uncomment to test):
    # query = "SELECT VERSION()"
    # results = execute_query(mydb, query)
    # if results:
    #     print(results)

    mydb.close()
