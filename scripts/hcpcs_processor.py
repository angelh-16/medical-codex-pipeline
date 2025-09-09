import pandas as pd

# Path to the HCPCS text file
file_path = "input/HCPC2025_OCT_ANWEB_v2.txt"

# Read the file into a DataFrame
# The file appears to be fixed-width formatted, so we'll use read_fwf

# You may need to adjust colspecs based on actual column widths
# Here is a simple guess based on the sample
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)


## save as csv to Module1_MedicalCodexes/hcpcs/output
output_path = "output/HCPC2025_OCT_ANWEB.csv"
df.to_csv(output_path, index=False)