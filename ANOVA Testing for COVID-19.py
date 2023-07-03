import pandas as pd
import scipy.stats as stats

# Load your dataset
df = pd.read_csv('Cleaned_Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv')
print(df.head())  # Print the first 5 rows of the dataframe

# Separate the death counts by age group
Group1 = df['COVID-19 Deaths'][df['Age Group'] == '0-24']
Group2 = df['COVID-19 Deaths'][df['Age Group'] == '25-34']
Group3 = df['COVID-19 Deaths'][df['Age Group'] == '35-44']
Group4 = df['COVID-19 Deaths'][df['Age Group'] == '45-54']
Group5 = df['COVID-19 Deaths'][df['Age Group'] == '55-64']
Group6 = df['COVID-19 Deaths'][df['Age Group'] == '65-74']
Group7 = df['COVID-19 Deaths'][df['Age Group'] == '75-84']
Group8 = df['COVID-19 Deaths'][df['Age Group'] == '85+']

# Perform the ANOVA
print(stats.f_oneway(Group1, Group2, Group3, Group4, Group5, Group6, Group7, Group8))  # Print the results of the ANOVA
