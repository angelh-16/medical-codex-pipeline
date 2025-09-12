import pandas as pd 

#import logging
import logging

#import save_to_formats function from common_functions.py
from utils.common_functions import save_to_formats

# Initialize logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("loinc_log.log"),
        logging.StreamHandler()
    ]
)

logging.info("Starting LOINC cleaning script")

# Load loinc csv file
try:
    loinc = pd.read_csv('input/Loinc.csv')
    logging.info(f"LOINC file loaded successfully with {loinc.shape[0]} rows and {loinc.shape[1]} columns")
except Exception as e:
    logging.error(f"Failed to read LOINC file: {e}")
    raise

# Info to describe 
loinc.info()

# Log the columns of the dataframe
logging.info(f"LOINC columns: {loinc.columns.tolist()}")

# Count of how many times each STATUS appears
count = loinc.STATUS.value_counts()
# Log the count
logging.info(f"STATUS value counts:\n{count}")

# Print first row
loinc.iloc[0]

# Check potential column names
loinc.LOINC_NUM
loinc.DefinitionDescription
loinc.LONG_COMMON_NAME

# Columns to keep
list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']
loinc_small = loinc[list_cols]
# Log the selected columns
logging.info(f"Selected columns: {list_cols}")

# Add new column for last updated date
loinc_small['last_updated'] = '09-07-2025'
# Log adding new column
logging.info("Added last_updated column")

# Rename columns
loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'Code',
    'LONG_COMMON_NAME': 'Description',
    'last_updated': 'Last Updated'
})
# Log renamed columns
logging.info("Renamed columns to 'Code', 'Description' and 'Last Updated'")

# Save cleaned dataset to csv & log the saving process
try:
    save_to_formats(loinc_small, 'loinc_small')
    logging.info("LOINC cleaned dataset saved successfully using save_to_formats")
except Exception as e:
    logging.error(f"Failed to save cleaned dataset: {e}")
    raise

logging.info("LOINC completed successfully")

# Save cleaned dataset to csv without using common function
# file_output_path = 'output/csv/loinc_small.csv'
# loinc_small.to_csv(file_output_path, index=False)