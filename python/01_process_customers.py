import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "customers_raw.csv"
OUTPUT_FILE = BASE_DIR / "output" / "customers_clean.csv"


def process_customers():

    print("Loading customer data...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Raw records: {len(df)}")

    # Remove whitespace from column names
    df.columns = df.columns.str.strip()

    # Remove whitespace from text columns
    text_columns = [
        "Customer_ID",
        "Customer_Name",
        "Email",
        "Country",
        "Customer_Status"
    ]

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    # Standardise customer status
    df["Customer_Status"] = (
        df["Customer_Status"]
        .str.upper()
    )

    # Standardise country
    df["Country"] = (
        df["Country"]
        .str.title()
    )

    # Convert registration date
    df["Registration_Date"] = pd.to_datetime(
        df["Registration_Date"],
        errors="coerce"
    )

    # Remove duplicate customers
    df = df.drop_duplicates(
        subset=["Customer_ID"],
        keep="first"
    )

    # Fill missing email
    df["Email"] = df["Email"].fillna(
        "unknown@example.com"
    )

    # Save cleaned data
    OUTPUT_FILE.parent.mkdir(
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Clean customer records: {len(df)}"
    )

    print(
        f"Output saved to: {OUTPUT_FILE}"
    )

    return df


if __name__ == "__main__":
    process_customers()
