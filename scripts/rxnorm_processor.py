import polars as pl
from pathlib import Path

file_path = Path('input/RXNATOMARCHIVE.RRF')

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

rxnorm = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

# Columns to keep
rxnorm_small = rxnorm[['rxaui', 'str']]

# Add new column for last updated date
rxnorm_small = rxnorm_small.with_columns(
    pl.lit('09-11-2025').alias('last_updated')
)

# Rename columns
rxnorm_small = rxnorm_small.rename({
    'rxaui' : 'Code',
    'str' : 'Description',
    'last_updated' : 'Last Updated'
})

# Save cleaned dataset to csv
output_dir = Path('output/csv/') 
output_dir.mkdir(exist_ok=True) 
output_path = output_dir / 'rxnorm_small.csv'

rxnorm_small.write_csv(output_path)

print(f"Successfully parsed {len(rxnorm_small)} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_path}")
print(f"Dataset shape: {rxnorm_small.shape}")
print(f"\nFirst 5 rows:")
print(rxnorm_small.head())
print(f"\nMemory usage (MB): {rxnorm_small.estimated_size() / 1024**2:.2f}")