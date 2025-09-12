import pandas as pd

# Import save_to_formats function from common_functions.py
from utils.common_functions import save_to_formats

file_path = 'input/icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

icd10who = pd.read_csv(file_path, sep=';', header=None, names=columns)

# Columns to keep
list_cols = ['icd10_code', 'title_en']
icd10who_small = icd10who[list_cols]

# Add new column for last updated date
icd10who_small['last_updated'] = '09-07-2025'

# Rename columns
icd10who_small = icd10who_small.rename(columns={
    'icd10_code': 'Code',
    'title_en': 'Description',
    'last_updated': 'Last Updated'
})

# Save cleaned dataset to csv
save_to_formats(icd10who_small, 'icd10who_small')

output_path = 'output/csv/icd10who_small.csv'
print(f"Successfully parsed {len(icd10who)} records from {file_path}")
print(f"Saved to {output_path}")
print(f"\nFirst 5 rows:")
print(icd10who.head())