import pandas as pd

# Import logging
import logging

# Import save_to_formats function from common_functions.py
from utils.common_functions import save_to_formats

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs.log"),
        logging.StreamHandler()
    ]
)

logging.info("Starting hcpcs cleaning script")

# Path to the HCPCS text file
file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"

# Adjusting colspecs based on actual column widths and column names
colspecs = [(0, 11), (11, 120), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]

# Read the file, colspecs, and column names into a DataFrame
try:
    hcpcs = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)
    logging.info(f"hcpcs file loaded successfully with {hcpcs.shape[0]} rows and {hcpcs.shape[1]} columns")
except Exception as e:
    logging.error(f"Failed to read hcpcs file: {e}")
    raise
# Info to describe 
hcpcs.info()

# Log the columns of the dataframe
logging.info(f"hcpcs columns: {hcpcs.columns.tolist()}")

# Columns to display
hcpcs_small = hcpcs[column_names]
logging.info(f"Selected columns: {column_names}")

# Add new column for last updated date
hcpcs_small['last_updated'] = '09-09-2025'
# Log adding new column
logging.info("Added last_updated column")

# Rename columns
hcpcs_small = hcpcs_small.rename(columns={
    'last_updated': 'Last Updated',
})
# Log renamed columns
logging.info("Renamed column to'Last Updated'")

# Save cleaned dataset to csv & log the saving process
try:
    save_to_formats(hcpcs_small, 'hcpcs_small')
    logging.info("hcpcs cleaned dataset saved successfully using save_to_formats")
except Exception as e:
    logging.error(f"Failed to save cleaned dataset: {e}")
    raise

logging.info("hcpcs completed successfully")
