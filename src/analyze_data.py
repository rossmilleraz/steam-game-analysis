import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

CLEAN_FILE = PROJECT_ROOT / "data" / "processed" / "steam_games_clean.csv"
OUTPUT_FOLDER = PROJECT_ROOT / "data" / "processed"


def analyze_steam_data():
    df = pd.read_csv(CLEAN_FILE)

    # Steam gives estimated owners as a range, like "100000 - 200000".
    # I am using the midpoint so I can use it as a number.
    owner_midpoints = []

    for value in df["estimated_owners"]:
        value = str(value).replace(",", "")

        if " - " in value:
            low, high = value.split(" - ")
            midpoint = (int(low) + int(high)) / 2
            owner_midpoints.append(midpoint)
        else:
            owner_midpoints.append(None)

    df["estimated_owners_midpoint"] = owner_midpoints

    # I wanted a simple way to compare regular games against stronger games.
    df["success_label"] = "Low / Unknown"

    df.loc[
        (df["review_pct"] >= 0.80) & (df["total_reviews"] >= 1000),
        "success_label"
    ] = "Successful"

    df.loc[
        (df["review_pct"] >= 0.90) & (df["total_reviews"] >= 10000),
        "success_label"
    ] = "Top Performer"

    # Price buckets make the price analysis easier to read.
    df["price_bucket"] = "Unknown"
    df.loc[df["price"] == 0, "price_bucket"] = "Free"
    df.loc[(df["price"] > 0) & (df["price"] <= 5), "price_bucket"] = "$0-$5"
    df.loc[(df["price"] > 5) & (df["price"] <= 15), "price_bucket"] = "$5-$15"
    df.loc[(df["price"] > 15) & (df["price"] <= 30), "price_bucket"] = "$15-$30"
    df.loc[(df["price"] > 30) & (df["price"] <= 60), "price_bucket"] = "$30-$60"
    df.loc[df["price"] > 60, "price_bucket"] = "$60+"

    df.to_csv(OUTPUT_FOLDER / "steam_games_analysis.csv", index=False)

    # Overall summary
    overall_summary = pd.DataFrame([{
        "total_games": len(df),
        "average_price": df["price"].mean(),
        "average_review_pct": df["review_pct"].mean(),
        "average_owners": df["estimated_owners_midpoint"].mean(),
        "average_peak_ccu": df["peak_ccu"].mean()
    }])

    overall_summary.to_csv(OUTPUT_FOLDER / "overall_summary.csv", index=False)

    # Genre summary
    genre_df = df.copy()
    genre_df["genres"] = genre_df["genres"].astype(str).str.split(",")
    genre_df = genre_df.explode("genres")
    genre_df["genres"] = genre_df["genres"].str.strip()

    genre_summary = genre_df.groupby("genres").agg(
        game_count=("name", "count"),
        avg_review_pct=("review_pct", "mean"),
        avg_price=("price", "mean"),
        avg_owners=("estimated_owners_midpoint", "mean")
    )

    genre_summary = genre_summary.reset_index()
    genre_summary = genre_summary.sort_values("game_count", ascending=False)
    genre_summary.to_csv(OUTPUT_FOLDER / "genre_summary.csv", index=False)

    # Price summary
    price_summary = df.groupby("price_bucket").agg(
        game_count=("name", "count"),
        avg_review_pct=("review_pct", "mean"),
        avg_owners=("estimated_owners_midpoint", "mean")
    )

    price_summary = price_summary.reset_index()
    price_summary.to_csv(OUTPUT_FOLDER / "price_summary.csv", index=False)

    # Yearly summary
    yearly_summary = df.groupby("release_year").agg(
        game_count=("name", "count"),
        avg_review_pct=("review_pct", "mean"),
        avg_price=("price", "mean")
    )

    yearly_summary = yearly_summary.reset_index()
    yearly_summary = yearly_summary.sort_values("release_year")
    yearly_summary.to_csv(OUTPUT_FOLDER / "yearly_summary.csv", index=False)

    # Top games
    top_games = df[df["total_reviews"] >= 1000]
    top_games = top_games.sort_values(
        ["review_pct", "total_reviews"],
        ascending=False
    )

    top_games.head(100).to_csv(
        OUTPUT_FOLDER / "top_reviewed_games.csv",
        index=False
    )

    print("Saved analysis files.")