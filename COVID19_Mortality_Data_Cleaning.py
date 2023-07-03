# Import necessary libraries
import pandas as pd

# Load the dataset
path = r"C:\Users\Jared King\Desktop\Covid-19 Project\Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv"
df = pd.read_csv(path)

# Remove rows where 'COVID-19 Deaths' contains the string 'One or more data cells'
df = df[~df['COVID-19 Deaths'].str.contains('One or more data cells', na=False)]
df = df[~df['Number of Mentions'].str.contains('One or more data cells', na=False)]

# Now it is safe to remove commas and convert to float
df['COVID-19 Deaths'] = df['COVID-19 Deaths'].str.replace(',', '').astype(float)
df['Number of Mentions'] = df['Number of Mentions'].str.replace(',', '').astype(float)

# Hypothesis 1: Age Group Comparison
valid_age_groups = ['0-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85+', 'Not stated', 'All Ages']
df = df[df['Age Group'].isin(valid_age_groups)]

# Hypothesis 2: Underlying Respiratory Conditions
valid_conditions = ['Influenza and pneumonia', 'Chronic lower respiratory diseases']
df = df[df['Condition'].isin(valid_conditions)]

# Hypothesis 3: Year Comparison
valid_years = df['Year'].dropna().unique().tolist()
df = df[df['Year'].isin(valid_years)]

# Remove rows where 'COVID-19 Deaths' or 'Number of Mentions' are NaN
df = df.dropna(subset=['COVID-19 Deaths', 'Number of Mentions'])

# Save the cleaned data
df.to_csv(r"C:\Users\Jared King\Desktop\Covid-19 Project\Cleaned_Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv", index=False)
