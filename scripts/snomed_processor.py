import polars as pl
from pathlib import Path

file_path = Path('input/sct2_Description_Full-en_US1000124_20250301.txt')

snomed = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    n_rows=10000,  # 10,000 rows because the full file is too large for git
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

# Columns to keep
snomed_small = snomed[['id', 'term']]

# Add new column for last updated date
snomed_small = snomed_small.with_columns(
    pl.lit('09-12-2025').alias('last_updated')
)

# Rename columns
snomed_small = snomed_small.rename({
    'id' : 'Code',
    'term' : 'Description',
    'last_updated' : 'Last Updated'
})

# Save cleaned dataset to csv
output_dir = Path('output/csv/')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'snomed_small.csv'

snomed_small.write_csv(output_path)

print(f"Successfully parsed {len(snomed_small)} records from SNOMED CT file")
print(f"Saved to {output_path}")
print(f"Dataset shape: {snomed_small.shape}")
print(f"\nColumn names: {snomed_small.columns}")
print(f"\nFirst 5 rows:")
print(snomed_small.head())
print(f"\nMemory usage (MB): {snomed_small.estimated_size() / 1024**2:.2f}")

print(f"\nActive terms count: {snomed.filter(pl.col('active') == 1).height}") # Can't get the term count to work with snomed_small
print(f"Language codes: {snomed['languageCode'].unique().to_list()}") # Can't get the language codes to work with snomed_small