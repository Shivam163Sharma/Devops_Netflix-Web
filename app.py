import psycopg2

# Replace these values with your actual database connection details
dbname = "DB_Netflix"
user = "Shivam101"
password = "Kwnsharma101"
host = "local_pgdb" # Usually "localhost" or "127.0.0.1" for a local database
port = "5432"  # Usually 5432 for PostgreSQL

# Define connection variable
connection = None
cursor = None

# Establish a connection to the database
try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Example: Execute a query
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"Connected to PostgreSQL database. Server version: {version}")

    # Don't forget to commit the changes
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print(f"Error connecting to PostgreSQL database: {error}")
    # Exit the script or handle the error accordingly

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")
