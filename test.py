import pandas as pd

# Load the CSV file
df = pd.read_csv('comp.csv')

# Get all unique values from the 'headquarters' column
unique_headquarters = df['headquarters'].dropna().unique()

# Sort them alphabetically
unique_headquarters.sort()

# Print each unique headquarters
print("Unique headquarters cities:")
for city in unique_headquarters:
    print(city)
