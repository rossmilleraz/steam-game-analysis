import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "steam_games_raw.csv"
CLEAN_FILE = PROJECT_ROOT / "data" / "processed" / "steam_games_clean.csv"


def clean_steam_data():
    df = pd.read_csv(RAW_FILE)

    # Make the column names easier to type and work with.
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Rename a few columns so the names make more sense to me.
    df = df.rename(columns={
        "appid": "app_id",
        "positive": "positive_reviews",
        "negative": "negative_reviews",
        "pct_pos_total": "review_pct",
        "num_reviews_total": "total_reviews"
    })

    # I am only keeping the columns that help answer the business question.
    keep_columns = [
        "app_id",
        "name",
        "release_date",
        "price",
        "developers",
        "publishers",
        "genres",
        "positive_reviews",
        "negative_reviews",
        "review_pct",
        "total_reviews",
        "estimated_owners",
        "average_playtime_forever",
        "peak_ccu",
        "recommendations"
    ]

    df = df[keep_columns]

    # Remove duplicate rows if they exist.
    df = df.drop_duplicates()

    # Convert dates so I can group games by release year later.
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df["release_year"] = df["release_date"].dt.year

    # Convert columns that should be numbers.
    number_columns = [
        "price",
        "positive_reviews",
        "negative_reviews",
        "review_pct",
        "total_reviews",
        "average_playtime_forever",
        "peak_ccu",
        "recommendations"
    ]

    for column in number_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Some games use negative values to mean the review data is unavailable.
    # Replace those values with missing values so they don't affect calculations.
    df.loc[df["total_reviews"] < 0, "total_reviews"] = pd.NA
    df.loc[df["review_pct"] < 0, "review_pct"] = pd.NA

    # This dataset stores review percentage as 0-100.
    # I changed it to 0-1 because that is easier to chart.
    df["review_pct"] = df["review_pct"] / 100

    df["price_type"] = "Paid"
    df.loc[df["price"] == 0, "price_type"] = "Free"

    CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_FILE, index=False)

    print(f"Saved cleaned file: {CLEAN_FILE}")