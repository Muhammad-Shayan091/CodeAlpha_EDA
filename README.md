# 🎬 Netflix EDA — Exploratory Data Analysis

![Netflix](https://img.shields.io/badge/Netflix-E50914?style=for-the-badge&logo=netflix&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)

> A complete Exploratory Data Analysis on the Netflix Movies & TV Shows dataset using Python, Pandas, NumPy and Matplotlib.

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

---

## 📂 Dataset

Dataset is **not included** in this repository due to size.

👉 Download from Kaggle: [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

| Detail | Info |
|---|---|
| File Name | `netflix_titles.csv` |
| Total Rows | ~8,807 titles |
| Total Columns | 12 |
| Source | Kaggle — Shivamb |

After downloading, place `netflix_titles.csv` in the same folder as `netflix_eda.py`.

---

## 📁 Project Structure

```
netflix-eda/
│
├── netflix_eda.py        ← Main EDA script
├── README.md             ← Project documentation
│
├── 01_content_type.png   ← Movies vs TV Shows
├── 02_content_per_year.png
├── 03_top_countries.png
├── 04_ratings.png
├── 05_top_genres.png
├── 06_movie_duration.png
├── 07_tv_seasons.png
├── 08_top_directors.png
├── 09_monthly_additions.png
├── 10_release_year.png
└── 11_correlation.png
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

---

## 💡 Key Insights

- 🎬 **Movies dominate** Netflix — ~70% of all content
- 🌍 **USA** is the top content-producing country
- 📅 Netflix content additions **peaked around 2019-2020**
- ⭐ **TV-MA** is the most common rating
- 🎭 **Dramas & Comedies** are the most popular genres
- ⏱️ Average movie duration is around **90 minutes**
- 📺 Most TV Shows have only **1 Season**

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

Made with ❤️ by **[Muhammad Shayan]**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)

---

⭐ **If you found this project helpful, please give it a star!** ⭐
