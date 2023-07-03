# Import necessary libraries
import pandas as pd

# Load the dataset
path = r"C:\Users\Jared King\Desktop\Covid-19 Project\Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv"
df = pd.read_csv(path)

# Print the types of values in each column
print("\nColumn Data Types:")
print(df.dtypes)

# Print time period covered
start_date = pd.to_datetime(df['Start Date']).min()
end_date = pd.to_datetime(df['End Date']).max()
print(f"\nThe dataset covers the period from {start_date} to {end_date}.")

# Print number of rows and columns
print(f"\nThe dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
