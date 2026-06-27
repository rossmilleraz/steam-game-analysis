# Steam Game Analysis

## Executive Summary

I wanted to see what separates successful Steam games from the thousands of other games on the platform. Instead of looking at one factor like price or review score, I wanted to compare several different metrics to see if there were any patterns.

The idea is to answer a question that could be useful to developers or publishers before releasing a game.

## Business Problem

Thousands of games are available on Steam, but only a small percentage become really successful. Pricing, genre, popularity, and player engagement all seem important, but it's not always clear which factors matter the most.

This project tries to answer one main question:

**What characteristics separate top-performing Steam games from the rest of the market?**

## Success Metrics

Instead of using just one number, I'm looking at several measurements of success.

* Positive review percentage
* Total reviews
* Estimated owners
* Peak concurrent players
* Average playtime

Looking at multiple metrics should give a better picture than relying on only one.

## Business Questions

These are the questions I'm trying to answer during the project.

* Which genres receive the highest review scores?
* Does price affect player satisfaction?
* Which genres have the highest player engagement?
* Do free games perform differently than paid games?
* What do the most successful games have in common?
* Are there any hidden gems with great reviews but relatively few owners?

## Methodology

### Data Cleaning

* Loaded the Steam dataset.
* Renamed columns to make them easier to work with.
* Removed duplicate records.
* Converted dates and numeric columns.
* Fixed missing and invalid review data.

### Analysis

After cleaning the data, I'll compare games by genre, price, popularity, review scores, and player engagement. I'll also look for trends over time and see if there are any relationships between these variables.

### Visualizations

I'll create Python charts to explore the data and then build an interactive Tableau dashboard once the analysis is finished.

## Key Findings

This section will be updated as I work through the analysis.

## Business Recommendations

Recommendations will be added after the final analysis.

## Next Steps

* Continue exploring the data.
* Improve the Python visualizations.
* Write SQL queries to answer the business questions.
* Build a Tableau dashboard.
* Summarize the final results.

## Dataset

**Source:** Steam Games Dataset (March 2025)

## Tech Stack

* Python
* Pandas
* Matplotlib
* SQL *(coming soon)*
* Tableau *(coming soon)*

## Screenshots

I'll add screenshots of the charts and dashboard once the project is finished.

## How to Run

1. Clone the repository.
2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Place the Steam dataset inside the `data/raw` folder.

4. Run the project.

```bash
python main.py
```
