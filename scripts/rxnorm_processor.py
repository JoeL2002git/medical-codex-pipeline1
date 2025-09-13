import polars as pl
from pathlib import Path

# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10


#Define file path
rxnorm_filepath = Path('inputs/RXN_Data/RXNCONSO.RRF')

##Define column names
columns = [
    'RXCUI', 'LAT', 'TS', 'LUI', 'STT', 'SUI', 'ISPREF', 'RXAUI', 'SAUI',
    'SCUI', 'SDUI', 'SAB', 'TTY', 'CODE', 'STR', 'SRL', 'SUPPRESS', 'CVF'
]
##Reading the file
df = pl.read_csv(rxnorm_filepath, separator='|', has_header=False, new_columns=columns)  


## only keep RXCUI and STR columns
df_small = df.select(['RXCUI', 'STR'])

## Rename columns to standard names
df_small = df_small.rename({
    'RXCUI': 'code',
    'STR': 'description'
})

## Add a 'last_updated' column with today's date
df_small = df_small.with_columns(pl.lit('2024-10-01').alias('last_updated'))

## Save as csv
output_path = Path('outputs/rxnorm_small.csv')
df_small.write_csv(output_path)



