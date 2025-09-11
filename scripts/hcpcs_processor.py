import pandas as pd

#import save_to_formats function from common_functions.py
from utils.common_functions import save_to_formats

# Path to the HCPCS text file
file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"

# Adjusting colspecs based on actual column widths and column names
colspecs = [(0, 11), (11, 120), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]

# Read the file, colspecs, and column names into a DataFrame
hcpcs = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)

# Info to describe 
hcpcs.info()

# Columns to display
hcpcs_small = hcpcs[column_names]

# Add new column for last updated date
hcpcs_small['Last_Updated'] = '09-09-2025'

# Save cleaned dataset to csv
save_to_formats(hcpcs_small, 'hcpcs_small')