import pandas as pd

file_path = 'inputs/icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(file_path, sep=';', header=None, names=columns)

## onle keep code and detailed_title columns
df = df[['code', 'detailed_title']].copy()

## rename detailed_title to description
df = df.rename(columns={'detailed_title': 'description'})

## add a 'last_updated' column with today's date
df['last_updated'] = '2024-10-01'

## create output path
output_path = 'outputs/icd10who_small.csv'
df.to_csv(output_path, index=False)

