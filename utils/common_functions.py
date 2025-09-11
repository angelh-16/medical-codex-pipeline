from pathlib import Path
import pandas as pd

def save_to_formats(df: pd.DataFrame, filename: str) -> None:
    # Ensure the output directory exists
    output_dir = Path('output') / 'csv'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Define file paths
    output_path = output_dir / f'{filename}.csv'

    # Save to CSV
    df.to_csv(output_path, index=False)