import polars as pl

npi_file_path = 'inputs/npidata_pfile_20050523-20250810.csv'

## just load the first 1000 rows
df = pl.read_csv(npi_file_path, n_rows=1000)

print(f"Successfully loaded {len(df)} records from NPI data")
print(f"Columns: {df.columns}")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())

print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")


df_polars_small = df.select([
    'NPI', 'Provider Last Name (Legal Name)'])


df_polars_small = df_polars_small.with_columns(
    pl.lit('2024-08-10').alias('last_updated')
)


df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
})

## save to CSV
outputs_path = 'outputs/npi_small.csv'
df_polars_small.write_csv(outputs_path)
