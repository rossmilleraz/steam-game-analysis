# Steam Game Analysis

## Executive Summary

I wanted to see what separates successful Steam games from the thousands of other games on the platform. Instead of looking at just one metric, I compared things like review scores, pricing, player engagement, and popularity to see if there were any clear patterns.

The goal is to answer a question that could be useful to developers or publishers before releasing a game.

---

## Business Problem

Steam has thousands of games across dozens of genres, but only a small percentage become highly successful. Developers have to make decisions about pricing, genre, and game design without always knowing which factors have the biggest impact.

This project focuses on one main question:

**What characteristics separate top-performing Steam games from the rest of the market?**

---

## Success Metrics

Rather than using a single metric, I looked at several measurements of success.

* Positive review percentage
* Total reviews
* Estimated owners
* Peak concurrent players (CCU)
* Average playtime

Using multiple metrics gives a better overall picture of how successful a game is.

---

## Business Questions

This project explores the following questions:

1. Which genres receive the highest review scores?
2. Does game price affect player satisfaction?
3. Which genres have the highest player engagement?
4. Do free games perform differently than paid games?
5. What do the most successful games have in common?
6. Which highly rated games have received relatively little attention?

---

## Methodology

### Data Cleaning

* Loaded the Steam Games dataset.
* Standardized column names.
* Removed duplicate records.
* Converted dates and numeric columns.
* Fixed missing and invalid review data.

### Exploratory Data Analysis

The data was explored using Python to answer each of the business questions above. Summary tables and visualizations were created to look for trends in genres, pricing, popularity, and player engagement.

### Visualization

Charts were created in Python using Matplotlib. An interactive Tableau dashboard will be added after the analysis is complete.

---

# Results

## Question 1

### Which genres receive the highest review scores?

**Chart**

*(Insert chart here)*

**Findings**

*Answer*

---

## Question 2

### Does game price affect player satisfaction?

**Chart**

*(Insert chart here)*

**Findings**

*Answer*

---

## Question 3

### Which genres have the highest player engagement?

**Chart**

*(Insert chart here)*

**Findings**

*Answer*

---

## Question 4

### Do free games perform differently than paid games?

**Chart**

*(Insert chart here)*

**Findings**

*Answer*

---

## Question 5

### What do the most successful games have in common?

**Chart**

*(Insert chart here)*

**Findings**

*Answer*

---

## Question 6

### Which highly rated games have received relatively little attention?

**Chart**

*(Insert chart here)*

**Findings**

*Answer*

---

## Business Recommendations

*Answer*

---

## Next Steps

* Finish exploratory data analysis.
* Complete the SQL portion of the project.
* Build an interactive Tableau dashboard.
* Summarize the final findings and recommendations.

---

## Dataset

**Source:** Steam Games Dataset (March 2025)

---

## Tech Stack

* Python
* Pandas
* Matplotlib
* SQL
* Tableau

---

## Screenshots

Screenshots will be added after the project is complete.

---

## How to Run

1. Clone the repository.
2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Place the Steam dataset in the `data/raw` folder.

4. Run the project.

```bash
python main.py
```
