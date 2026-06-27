# This file runs the whole project from start to finish.
# One main file so I do not have to run every script manually

from src.clean_data import clean_steam_data
from src.analyze_data import analyze_steam_data

# Keeping it here because I want to keep the code, but I stopped using the make_charts.py and used notebooks instead
# from src.make_charts import make_charts


def main():
    print("Cleaning data...")
    clean_steam_data()

    print("Analyzing data...")
    analyze_steam_data()

    print("Making charts...")
    # make_charts()

    print("Done.")


if __name__ == "__main__":
    main()
