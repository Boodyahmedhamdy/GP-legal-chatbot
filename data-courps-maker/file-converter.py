import csv

# # Get the file name from the user
# file_name = input("Enter the name of the .txt file you want to convert: ")
#
# # Open the .txt file in read mode, specifying encoding for Arabic text
# with open(file_name, "r", encoding="utf-8") as txt_file:
#    print("Reading content from .txt file...")
#
#    # Create a new .csv file with the same name, replacing the extension
#    csv_file = f"{file_name.split('.')[0]}.csv"
#    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
#        print(f"Creating new .csv file: {csv_file}")
#
#        # Create a CSV writer object
#        csv_writer = csv.writer(csvfile)
#
#        # Read each line from the .txt file, split by tabs, and write to the CSV file
#        for line in txt_file:
#            csv_writer.writerow(line.strip().split("\t"))
#            print(f"Wrote line to CSV: {line.strip()}")
#
# print("Conversion complete!")
#

import pandas as pd

def read_xlsx_file1(file_path):
    """Reads an XLSX file using pandas and returns the data as a DataFrame."""

    print(f"Reading content from XLSX file: {file_path}")

    try:
        df = pd.read_excel(file_path)
        print("XLSX file read successfully!")
        return df

    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None

    except pd.errors.ParserError:
        print(f"Error: Invalid format or corrupted XLSX file: {file_path}")
        return None


import pandas as pd

def read_xlsx_file(file_path):
    """Reads an .xlsx file with Arabic text using pandas.

    Args:
        file_path (str): The path to the .xlsx file.

    Returns:
        pd.DataFrame: The DataFrame containing the data from the .xlsx file.
    """

    print(f"Reading .xlsx file: {file_path}")

    # Use 'openpyxl' engine for better Arabic text handling
    try:
        df = pd.read_excel(file_path, engine='openpyxl')

    except ValueError:
        print("Incorrect file path or file format. Please check and try again.")
        return None

    print("DataFrame created from .xlsx file:")
    print(df)

    return df


df = read_xlsx_file("initial.xlsx")
df.to_csv("test.csv")


# df = pd.read_csv("New Text Document.csv")
# print(
#     df.columns,
#     df.head()['إجابة']
#
# )