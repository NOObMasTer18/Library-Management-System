from dotenv import load_dotenv
import pymysql
import os



# environment variables
load_dotenv()
user = os.getenv("User")
myDatabase=os.getenv("myDatabase")
dbPassword = os.getenv("Password")
host = os.getenv("Host")

#Constructs 
def get_connection() ->  pymysql.connect:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=dbPassword,
        database=myDatabase
    )
    
    return connection

def get_connectionAndCursor() -> tuple[pymysql.connect.cursor,pymysql.connect]:
    connection = get_connection()
    connection.ping()
    cursor = connection.cursor()
    return connection,cursor


# Check
if __name__ == "__main__":
    connection,cursor = get_connectionAndCursor()
    cursor.execute("select version()")
    for x in cursor:
        print(f"Connected successfully with MySql{x}!")