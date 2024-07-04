import os
from dotenv import load_dotenv
import pyodbc
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
server = os.getenv('DB_SERVER')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')

# Define the connection string
connection_string = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={user};"
    f"PWD={password}"
)

# Establish the connection
conn = pyodbc.connect(connection_string)

# Query to retrieve the first dataset
query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"

# Execute the query and fetch the data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Display the first few rows of the DataFrame
print(df.head())

# Optionally, save the data to a CSV file for further analysis
df.to_csv('data/churn_first_3000.csv', index=False)