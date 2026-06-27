# import pandas as pd
# import matplotlib.pyplot as plt
# from pathlib import Path
#
#
# PROJECT_ROOT = Path(__file__).resolve().parents[1]
#
# DATA_FOLDER = PROJECT_ROOT / "data" / "processed"
# CHART_FOLDER = PROJECT_ROOT / "outputs" / "charts"
#
#
# def make_charts():
#     CHART_FOLDER.mkdir(parents=True, exist_ok=True)
#
#     df = pd.read_csv(DATA_FOLDER / "steam_games_analysis.csv")
#     genre_summary = pd.read_csv(DATA_FOLDER / "genre_summary.csv")
#     price_summary = pd.read_csv(DATA_FOLDER / "price_summary.csv")
#     yearly_summary = pd.read_csv(DATA_FOLDER / "yearly_summary.csv")
#
#     blue = "#2F80ED"
#     green = "#27AE60"
#     orange = "#F2994A"
#     purple = "#9B51E0"
#
#     # Games released over time
#     plt.figure(figsize=(10, 6))
#     plt.plot(yearly_summary["release_year"], yearly_summary["game_count"], color=blue)
#     plt.title("Steam Game Releases Over Time")
#     plt.xlabel("Release Year")
#     plt.ylabel("Number of Games")
#     plt.grid(alpha=0.3)
#     plt.tight_layout()
#     plt.savefig(CHART_FOLDER / "releases_over_time.png")
#     plt.close()
#
#     # Top genres
#     top_genres = genre_summary.head(10)
#
#     plt.figure(figsize=(10, 6))
#     plt.barh(top_genres["genres"], top_genres["game_count"], color=purple)
#     plt.title("Top 10 Steam Genres by Game Count")
#     plt.xlabel("Number of Games")
#     plt.ylabel("Genre")
#     plt.gca().invert_yaxis()
#     plt.tight_layout()
#     plt.savefig(CHART_FOLDER / "top_genres.png")
#     plt.close()
#
#     # Review score by price bucket
#     plt.figure(figsize=(10, 6))
#     plt.bar(price_summary["price_bucket"], price_summary["avg_review_pct"], color=green)
#     plt.title("Average Review Score by Price Bucket")
#     plt.xlabel("Price Bucket")
#     plt.ylabel("Average Review Score")
#     plt.ylim(0, 1)
#     plt.tight_layout()
#     plt.savefig(CHART_FOLDER / "review_by_price_bucket.png")
#     plt.close()
#
#     # Price vs review score
#     scatter_df = df[(df["price"] <= 100) & (df["total_reviews"] >= 100)]
#
#     plt.figure(figsize=(10, 6))
#     plt.scatter(scatter_df["price"], scatter_df["review_pct"], color=orange, alpha=0.3)
#     plt.title("Price vs Review Score")
#     plt.xlabel("Price")
#     plt.ylabel("Review Score")
#     plt.ylim(0, 1)
#     plt.grid(alpha=0.3)
#     plt.tight_layout()
#     plt.savefig(CHART_FOLDER / "price_vs_review_score.png")
#     plt.close()
#
#     print("Saved charts.")