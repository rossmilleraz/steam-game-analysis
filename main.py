# This file runs the whole project from start to finish.
# One main file so I do not have to run every script manually

def main():
    print("Cleaning Steam data...")
    clean_steam_data()

    print("Creating summary tables.")
    create_summary_tables()

    print("Creating charts.")
    create_charts()

    print("Project finished.")


if __name__ == "__main__":
    main()
