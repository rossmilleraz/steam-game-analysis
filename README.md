# Steam Game Analysis

## Executive Summary

This project explores the Steam Games dataset to identify the characteristics that separate top-performing games from the rest of the market. The goal is to uncover trends in pricing, genres, player engagement, and review scores that could help developers and publishers better understand what contributes to a game's success on Steam.

## Business Problem

Thousands of games are released on Steam every year, making it difficult for developers and publishers to understand what factors contribute to strong performance. The central question this project addresses is:

**What characteristics separate top-performing Steam games from the rest of the market?**

## Methodology

### Data Loading & Cleaning

* Loaded the March 2025 Steam Games dataset.
* Renamed and standardized column names.
* Removed duplicate records.
* Converted dates and numeric columns into appropriate data types.
* Selected the most relevant columns for analysis.

### Data Analysis

* Created price buckets for comparison.
* Calculated estimated owner midpoints from owner ranges.
* Grouped games by genre, release year, and price range.
* Generated summary tables for further analysis.

### Visualization

* Steam game releases over time.
* Top Steam genres by number of games.
* Average review score by price range.
* Price vs. review score.
* Additional visualizations will be added as the project progresses.

## Key Findings

*This section will be updated as the analysis is completed.*

## Business Recommendations

*This section will be updated after the analysis is complete.*

## Next Steps

* Expand exploratory data analysis.
* Perform SQL analysis to answer additional business questions.
* Build an interactive Tableau dashboard.
* Identify key characteristics shared by successful Steam games.
* Finalize recommendations based on project findings.

## Dataset

**Source:** Steam Games Dataset (March 2025)

## Tech Stack

* Python – Data cleaning and analysis
* Pandas – Data manipulation
* Matplotlib – Data visualization
* SQL *(planned)*
* Tableau *(planned)*

## Screenshots

*Visualizations will be added as the project progresses.*

## How to Run

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Place the Steam dataset in the `data/raw` folder.
4. Run the project:

```bash
python main.py
```

