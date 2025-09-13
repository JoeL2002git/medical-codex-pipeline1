import pandas as pd 

## input file path
file_path= 'inputs/icd10cm_order_2025.csv'

## read file path
icd10cm = pd.read_csv(file_path)

## only keep code and description columns
icdcodes = icd10cm[['code', 'description']].copy()

## remove the first row (header row)
icdcodes = icdcodes.iloc[1:]

## add a 'last_updated' column with today's date
icdcodes['last_updated'] = '2024-10-01'

## change to string type
icdcodes['code'] = icdcodes['code'].astype(str)
icdcodes['description'] = icdcodes['description'].astype(str)

## remove leading and trailing whitespace from the description column
icdcodes['description'] = icdcodes['description'].str.strip()

## remove leading and trailing whitespace from the code column
icdcodes['code'] = icdcodes['code'].str.strip()

## save as csv
output_path = 'outputs/icd10cm_small.csv'
icdcodes.to_csv(output_path, index=False)