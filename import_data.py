import io
import os
import pandas as pd

def main():
    data_folder = "data"

    excel_files = [
        "game-log_21-22.xlsx",  # <-- these are actually HTML files despite .xlsx
        "game-log_22-23.xlsx",
        "game-log_23-24.xlsx",
        "game-log_24-25.xlsx",
        "game-log_24-playoffs.xlsx"
    ]

    dataframes = []

    for file_name in excel_files:
        file_path = os.path.join(data_folder, file_name)

        # 1) Read the entire file as a *string*, ignoring its extension
        with open(file_path, "r", encoding="utf-8") as f:
            file_contents = f.read()

        # 2) Convert that string into a "file-like" object using StringIO
        html_data = io.StringIO(file_contents)

        # 3) Parse with pd.read_html on the string content
        #    - This returns a list of DataFrames, because one HTML doc can have multiple <table> tags
        df_list = pd.read_html(html_data)

        # 4) If you only expect one table, grab df_list[0]
        df = df_list[0]

        # 5) Add a season column if needed
        if "21-22" in file_name:
            df["season"] = "2021-22"
        elif "22-23" in file_name:
            df["season"] = "2022-23"
        elif "23-24" in file_name:
            df["season"] = "2023-24"
        elif "24-25" in file_name:
            df["season"] = "2024-25"
        elif "playoffs" in file_name:
            df["season"] = "2024 playoffs"

        dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)

    print("Combined DataFrame Info:")
    print(combined_df.info())
    print("\nFirst 5 rows of the combined DataFrame:")
    print(combined_df.head())

if __name__ == "__main__":
    main()
