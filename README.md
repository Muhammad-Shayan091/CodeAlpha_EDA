# 🎬 Netflix EDA — Exploratory Data Analysis

![Netflix](https://img.shields.io/badge/Netflix-E50914?style=for-the-badge&logo=netflix&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)

> A complete Exploratory Data Analysis on the Netflix Movies & TV Shows dataset using Python, Pandas, NumPy and Matplotlib — uncovering 20 unique insights!

---

## 📌 Table of Contents
- [About the Project](#-about-the-project)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Analysis Steps](#-analysis-steps)
- [Key Insights](#-key-insights)
- [How to Run](#-how-to-run)
- [Libraries Used](#-libraries-used)

---

## 📖 About the Project

This project performs a full EDA on Netflix's content library to uncover trends, patterns and insights such as:
- What type of content dominates Netflix?
- Which countries produce the most content?
- How has Netflix grown over the years?
- What are the most popular genres and ratings?
- Which actors appear most on Netflix?
- How do genre trends change over years?
- What is the best month to release content?
- How does content vary across decades?

---

## 📂 Dataset

Dataset is **not included** in this repository due to size.

👉 Download from Kaggle: [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

| Detail | Info |
|---|---|
| File Name | `netflix_titles.csv` |
| Total Rows | ~8,800 titles |
| Total Columns | 12 |
| Source | Kaggle — Shivamb |

After downloading, place `netflix_titles.csv` in the same folder as `p.py`.

---

## 📁 Project Structure

```
netflix-eda/
│
├── p.py                      ← Main EDA script
├── README.md                 ← Project documentation
│
├── 01_content_type.png       ← Movies vs TV Shows
├── 02_content_per_year.png   ← Content added per year
├── 03_top_countries.png      ← Top 15 countries
├── 04_ratings.png            ← Ratings distribution
├── 05_top_genres.png         ← Top 15 genres
├── 06_movie_duration.png     ← Movie duration histogram
├── 07_tv_seasons.png         ← TV show seasons
├── 08_top_directors.png      ← Top 10 directors
├── 09_monthly_additions.png  ← Monthly content additions
├── 10_release_year.png       ← Release year trend
├── 11_correlation.png        ← Correlation heatmap
├── 12_top_actors.png         ← Top 10 actors
├── 13_country_comparison.png ← India vs USA vs Korea
├── 14_genre_trends.png       ← Genre trends over years
├── 15_best_month.png         ← Best month to release
└── 16_content_per_decade.png ← Content per decade
```

---

## 🔍 Analysis Steps

| Step | Description |
|---|---|
| 1 | Load Dataset |
| 2 | Data Overview — shape, dtypes, nulls |
| 3 | Data Cleaning — missing values, duplicates, dates |
| 4 | Movies vs TV Shows Distribution |
| 5 | Content Added Per Year |
| 6 | Top Content-Producing Countries |
| 7 | Ratings Distribution |
| 8 | Top Genres |
| 9 | Movie Duration Analysis |
| 10 | TV Show Seasons Analysis |
| 11 | Top Directors |
| 12 | Monthly Content Additions |
| 13 | Release Year Trend |
| 14 | Correlation Analysis |
| 15 | Final Insights Summary |
| 16 | Top Actors Analysis |
| 17 | India vs USA vs Korea Comparison |
| 18 | Genre Trends Over Years |
| 19 | Best Month to Release Content |
| 20 | Content Per Decade (1950s–2020s) |

---

## 💡 Key Insights

- 🎬 **Movies dominate** Netflix — ~70% of all content
- 🌍 **USA** is the top content-producing country
- 📅 Netflix content additions **peaked around 2019-2020**
- ⭐ **TV-MA** is the most common rating
- 🎭 **Dramas & Comedies** are the most popular genres
- ⏱️ Average movie duration is around **90 minutes**
- 📺 Most TV Shows have only **1 Season**
- 🎭 **Anupam Kher** is among the most featured actors on Netflix
- 🇰🇷 **Korea's K-Drama** boom is clearly visible in genre trends
- 📅 **January & December** are peak months for content addition
- 📆 **2010s decade** has the most content on Netflix
- 🔗 Release year & year added have **almost no correlation (0.01)** — Netflix adds old & new content equally

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/netflix-eda.git
cd netflix-eda
```

**2. Install required libraries**
```bash
pip install pandas numpy matplotlib
```

**3. Download the dataset**

👉 [Netflix Dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

Place `netflix_titles.csv` in the project folder.

**4. Run the script**
```bash
python netflix_eda.py
```

All charts will be automatically saved as PNG files. ✅

---

## 🛠️ Libraries Used

| Library | Purpose |
|---|---|
| `pandas` | Data loading, cleaning, analysis |
| `numpy` | Numerical computations, statistics |
| `matplotlib` | Data visualization & charts |

---

## 👤 Author

Made with ❤️ by **[MUHAMMAD SHAYAN]**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)

---

⭐ **If you found this project helpful, please give it a star!** ⭐