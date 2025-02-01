import pandas as pd
from sqlalchemy import create_engine

# Replace the following with your database connection details
username = 'root'  # Your MySQL username
password = '1234'  # Your MySQL password
host = 'localhost'  # Your MySQL host, e.g., 'localhost' or an IP address
database = 'Sample'  # Your MySQL database name

# Create a connection string using SQLAlchemy
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

# Create an engine
query = create_engine(connection_string)

# Read data from MySQL into a pandas DataFrame
sql_df = pd.read_sql('SELECT * FROM Products', query)

csv_df=pd.read_csv(r"C:\Users\CVR\Desktop\Sales.csv")

merged_df=pd.merge(sql_df,csv_df,on='ProductID',how='outer')

# Display the DataFrame
print(merged_df)
