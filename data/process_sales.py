import pandas as pd
import glob
import os


def clean_data(df):
    # Check column name (try both possibilities)
    if "product" in df.columns:
        df = df[df["product"] == "pink morsel"]
    elif "products" in df.columns:
        df = df[df["products"] == "pink morsel"]
    else:
        print("⚠️ No 'product' or 'products' column found.")
        return pd.DataFrame(columns=["sales", "date", "region"])

    # Clean price
    df["price"] = df["price"].str.replace('$', '', regex=False)
    df["price"] = df["price"].apply(lambda x: float(x.split('.')[0] + '.' + x.split('.')[1][:2]))
    df["price"] = pd.to_numeric(df["price"], errors='coerce')

    df["sales"] = df["quantity"] * df["price"]
    return df[["sales", "date", "region"]]


def combine_and_save(file_list, output_name):
    combined = []
    for file in file_list:
        df = pd.read_csv(file)
        cleaned_df = clean_data(df)
        combined.append(cleaned_df)

    if not combined:
        print("⚠️ No data to combine. Check if CSV files contain 'pink morsel'.")
        return

    final_df = pd.concat(combined, ignore_index=True)
    final_df.to_csv(output_name, index=False)
    print(f"✅ Combined data saved to {output_name}")


if __name__ == "__main__":
    # CSV files are in the same folder as this script
    files = glob.glob("*.csv")
    print(f"📁 Found {len(files)} CSV files.")
    combine_and_save(files, "final_sales.csv")