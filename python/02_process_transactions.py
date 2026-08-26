import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "transactions_raw.csv"
OUTPUT_FILE = BASE_DIR / "output" / "transactions_clean.csv"


def process_transactions():

    print("Loading transaction data...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Raw records: {len(df)}")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean text columns
    text_columns = [
        "Transaction_ID",
        "Customer_ID",
        "Product"
    ]

    for column in text_columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
        )

    # Convert numeric columns
    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    )

    df["Unit_Price"] = pd.to_numeric(
        df["Unit_Price"],
        errors="coerce"
    )

    # Convert transaction date
    df["Transaction_Date"] = pd.to_datetime(
        df["Transaction_Date"],
        errors="coerce"
    )

    # Remove duplicate transaction IDs
    df = df.drop_duplicates(
        subset=["Transaction_ID"],
        keep="first"
    )

    # Remove invalid quantities
    df = df[
        df["Quantity"] > 0
    ]

    # Remove invalid prices
    df = df[
        df["Unit_Price"] > 0
    ]

    # Calculate revenue
    df["Revenue"] = (
        df["Quantity"]
        * df["Unit_Price"]
    )

    # Sort by transaction date
    df = df.sort_values(
        "Transaction_Date"
    )

    OUTPUT_FILE.parent.mkdir(
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Clean transaction records: {len(df)}"
    )

    print(
        f"Output saved to: {OUTPUT_FILE}"
    )

    return df


if __name__ == "__main__":
    process_transactions()
