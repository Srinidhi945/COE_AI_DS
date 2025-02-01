import pandas as pd
import numpy as np
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

xlsx_df=pd.read_excel(r"C:\Users\CVR\Desktop\Inventory.xlsx")

merged_df1 = pd.merge(sql_df, csv_df, on='ProductID', how='outer')
df = pd.merge(merged_df1, xlsx_df, on='ProductID', how='outer')

# Display the DataFrame
print(df)

print("*******************************************************************************************************************")

print("dtype:",df.dtypes)
print("_________________________________________________________")
print(f"Memory usage:{df.memory_usage(deep=True)}")
print("_________________________________________________________")
print("dtype of price is :",df['Price'].dtypes)
print("_________________________________________________________")
print(f"Memory usage:{df['Price'].memory_usage(deep=True)}")
df['Price']=df['Price'].astype(np.int16)
print("_________________________________________________________")
print(f"Memory usage:{df['Price'].memory_usage(deep=True)}")
print("_________________________________________________________")
print("dtype of price is :",df['Price'].dtypes)
print("*******************************************************************************************************************")
print("dtype of TotalSale is :",df['SaleID'].dtypes)
print("_________________________________________________________")
print(f"Memory usage:{df['SaleID'].memory_usage(deep=True)}")
df['SaleID']=df['SaleID'].astype(np.float32)
print("_________________________________________________________")
print(f"Memory usage:{df['SaleID'].memory_usage(deep=True)}")
print("dtype of TotalSale is :",df['TotalSale'].dtypes)
print("*******************************************************************************************************************")
#converting in to float and float to int in order to manage memory 