import pandas as pd 

# Load loinc csv file
loinc = pd.read_csv('input/Loinc.csv')

# Info to describe 
loinc.info()

# Count of how many times each STATUS appears
loinc.STATUS.value_counts()

# Print first row
loinc.iloc[0]

# Check potential column names
loinc.LOINC_NUM
loinc.DefinitionDescription
loinc.LONG_COMMON_NAME

# Columns to keep
list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']
loinc_small = loinc[list_cols]

# Add new column for last updated date
loinc_small['last_updated'] = '09-07-2025'

# Rename columns
loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description',
})

# Save cleaned dataset to csv
file_output_path = 'output/loinc_small.csv'

loinc_small.to_csv(file_output_path, index=False)