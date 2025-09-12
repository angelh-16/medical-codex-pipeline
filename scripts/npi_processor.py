import polars as pl
import pandas as pd
import time

npi_file_path = 'input/npidata_pfile_20050523-20250810.csv'

# Just load the first 1000 rows
df_polars = pl.read_csv(npi_file_path, n_rows=1_000) # Python kept crashing with the n_row set to 1_000_000

start = time.time()
df_polars = pl.read_csv(npi_file_path, n_rows=1_000) # Python kept crashing with the n_row=1_000_000
end = time.time()
elapsed_time_polars = end - start
print(elapsed_time_polars)

start = time.time()
df_pandas = pd.read_csv(npi_file_path, nrows=1000, low_memory=False) # Python kept crashing with the nrow=1000000
elapsed_time_pandas = end - start
print(elapsed_time_pandas)

print(f"Successfully loaded {len(df_polars)} records from NPI data")
print(f"Columns: {df_polars.columns}")
print(f"\nDataset shape: {df_polars.shape}")
print(f"\nFirst 5 rows:")
print(df_polars.head())

print(f"\nMemory usage (MB): {df_polars.estimated_size() / 1024**2:.2f}")

# Columns to keep
df_polars_small = df_polars.select([
    'NPI', 
    'Provider Last Name (Legal Name)'
])

# Add new column for last updated date
df_polars_small = df_polars_small.with_columns(
    pl.lit('09-11-2025').alias('last_updated')
)

# Rename colummns
df_polars_small = df_polars_small.rename({
    'NPI': 'Code',
    'Provider Last Name (Legal Name)': 'Description',
    'last_updated': 'Last Updated'
})

# Save cleaned dataset to csv
output_path = 'output/csv/npi_small.csv'
df_polars_small.write_csv(output_path)
df_polars_small.write_parquet('output/csv/npi_small.parquet')
