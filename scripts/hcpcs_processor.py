import pandas as pd

# Path to the HCPCS text file
file_path = "inputs/HCPC2025_OCT_ANWEB.csv"

# Read the file into a DataFrame
## the file appears to be fixed-width formatted, so we'll use read_fwf
hcpc = pd.read_fwf(file_path)

## adjust colspecs and column names as needed based on actual file structure
colspecs = [(0, 8), (9, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)

## only keep Code and Description1 columns
df = df[['Code', 'Description1']] 

## add a 'last_updated' column with today's date
df['last_updated'] = '2024-10-01'

##rename columns to standard names
df = df.rename(columns={
    'Code': 'code',
    'Description1': 'description'
})

##remove the first row
df = df.iloc[1:]

## save as csv
output_path = "outputs/hcpcs_small.csv"
df.to_csv(output_path, index=False)

