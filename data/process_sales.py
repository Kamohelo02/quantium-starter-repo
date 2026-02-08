import pandas as pd
import glob

def clean_data(df):
    # keep rows where product is pink morsel
    df = df[df["product"] == "pink morsel"]
    # create sales column
    df["sales"] = df["quantity"] * df["price"]
    # keep only columns we need
    return df[["sales", "date", "region"]]

def combine_and_save(file_list, output_name):
    # reads every csv file in file_list and cleans it, merge it, and save to output_name
    combined = []
    for file in file_list:
        df = pd.read_csv(file)
        cleaned_df = clean_data(df)
        combined.append(cleaned_df)

    # merge all dataframes
    final_df = pd.concat(combined, ignore_index=True)
    # save to csv
    final_df.to_csv(output_name, index=False)
    print(f"Combined data saved to {output_name}")

if __name__ == "__main__":
    # find all csv files in data folder
    files = glob.glob("*.csv")
    # check if files are found
    print(f"Found {len(files)} files")
    # call the function
    combine_and_save(files, "final_sales.csv")



