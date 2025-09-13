import pandas as pd

def save_to_formats(df, base_filename):
    """
    Save the DataFrame to a CSV file.
    Args:
        df (pd.DataFrame): The DataFrame to save.
        base_filename (str): The base filename (without extension).
    """
    csv_path = f"{base_filename}.csv"
    df.to_csv(csv_path, index=False)