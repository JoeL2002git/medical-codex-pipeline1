import pandas as pd

file_path = 'inputs/Snowmed_Data/Full/Terminology/sct2_Description_Full-en_US1000124_20250901.txt'

# Read the first 10,000 rows
df = pd.read_csv(file_path, sep='\t', nrows=10000)

# Only keep conceptId and term columns
df_small = df[['conceptId', 'term']].copy()

# Rename columns to standard names
df_small = df_small.rename(columns={
    'conceptId': 'code',
    'term': 'description'
})

# Add a 'last_updated' column with today's date
df_small['last_updated'] = '2024-10-01'

# Save as CSV
output_path = 'outputs/snowmed_small.csv'
df_small.to_csv(output_path, index=False)