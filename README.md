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

> Each insight answers **what was found**, **why it happened**, and **what it means for the business**.

---

### 🎬 Insight 1 — Movies Dominate Netflix (~70%)
**What:** Movies make up nearly 70% of Netflix's total content library.

**Why it occurs:** Movies are cheaper and faster to license than multi-season TV shows. Netflix can add hundreds of movies from studios worldwide with a single licensing deal, while a TV show requires ongoing production, cast contracts, and episode-by-episode costs.

**Business impact:** Netflix's strategy is to use movies as volume fillers to keep the library large and diverse, while using original TV shows as the primary tool to retain subscribers long-term.

---

### 🌍 Insight 2 — USA is the Top Content Producer
**What:** The United States produces more Netflix content than any other country by a significant margin.

**Why it occurs:** Hollywood is the world's largest and most established entertainment industry. Netflix's headquarters is in the USA, giving it easier access to American studios, talent, and production infrastructure. Additionally, English-language content has global appeal.

**Business impact:** Netflix's heavy dependence on US content is a strategic risk — if Hollywood studios pull their content (as Disney, NBC did with Disney+ and Peacock), Netflix's library shrinks drastically. This is why Netflix invested heavily in original content production.

---

### 📅 Insight 3 — Content Peaked in 2019–2020
**What:** Netflix added the highest number of titles in 2019 and 2020.

**Why it occurs:** Two reasons — first, Netflix was in an aggressive global expansion phase, spending billions on content to enter new markets. Second, the COVID-19 pandemic in 2020 caused a massive surge in streaming demand as people stayed home, pushing Netflix to fast-track content additions.

**Business impact:** Post-2020, content additions slowed because Netflix shifted focus from quantity to quality, and competition from Disney+, HBO Max, and Prime Video forced a more strategic approach to content investment.

---

### ⭐ Insight 4 — TV-MA is the Most Common Rating
**What:** TV-MA (Mature Audiences only) is Netflix's most frequently used content rating.

**Why it occurs:** Netflix's primary subscriber base is adults aged 18–35. Adult-oriented content (crime dramas, thrillers, dark comedies) generates more engagement and social media buzz than family-friendly content. Shows like Ozark, Breaking Bad, and Narcos — all TV-MA — became viral hits that drove subscriptions.

**Business impact:** Netflix's content strategy deliberately targets mature audiences because they are the most consistent paying subscribers. Family content serves a secondary purpose of reducing churn among households with children.

---

### 🎭 Insight 5 — Dramas & Comedies Dominate Genres
**What:** Dramas and Comedies are the most listed genres across both movies and TV shows on Netflix.

**Why it occurs:** These are universally appealing genres that transcend cultural and language barriers. A drama or comedy from India, Korea, or Spain can find a global audience, making them cost-effective investments for Netflix's international strategy.

**Business impact:** Netflix's genre-heavy investment in Drama explains why the platform has been so successful with international originals like Money Heist, Squid Game, and Sacred Games — all dramas that became global phenomena.

---

### ⏱️ Insight 6 — Average Movie Duration is ~90 Minutes
**What:** Most Netflix movies are approximately 90 minutes long.

**Why it occurs:** 90 minutes is the industry "sweet spot" validated by decades of cinema data — long enough for a complete story arc, but short enough to watch in one sitting. Netflix's algorithm also favors completion rates — shorter movies get watched fully, boosting engagement metrics.

**Business impact:** Netflix uses completion rate as a key metric to decide which movies to renew or recommend. A 3-hour film that 60% of viewers abandon is algorithmically penalized compared to a 90-minute film with 90% completion.

---

### 📺 Insight 7 — Most TV Shows Have Only 1 Season
**What:** The majority of Netflix TV shows consist of only 1 season.

**Why it occurs:** Netflix cancels shows aggressively based on viewership data from the first season. If a show doesn't attract enough viewers in its launch window, it gets cancelled before a second season is greenlit. This is Netflix's "fail fast" content strategy.

**Business impact:** This causes frustration among viewers (many beloved shows cancelled after Season 1), but it protects Netflix from the financial risk of investing in multi-season productions that don't scale. It also keeps the content library fresh with new titles.

---

### 🎭 Insight 8 — Anupam Kher is Among Most Featured Actors
**What:** Anupam Kher appears in more Netflix titles than almost any other actor.

**Why it occurs:** Bollywood produces an enormous volume of films annually, and Anupam Kher is one of the most prolific character actors in Indian cinema with 500+ film credits. Since Netflix acquired a large catalog of Bollywood content, actors with high film counts naturally appear frequently.

**Business impact:** This highlights Netflix's massive push into the Indian market — India is one of Netflix's largest growth markets, and stocking Bollywood content is a key strategy to acquire and retain Indian subscribers.

---

### 🇰🇷 Insight 9 — Korea's K-Drama Boom is Visible
**What:** Korean content, especially TV Shows, has grown dramatically in Netflix's library post-2019.

**Why it occurs:** Squid Game (2021) became the most-watched Netflix show in history, proving that non-English content could achieve global scale. This success caused Netflix to massively increase investment in Korean originals. Korea also has a mature, high-quality production industry that delivers content at lower cost than Hollywood.

**Business impact:** Netflix now invests over $500M annually in Korean content. The K-Drama boom proves that subtitles are no longer a barrier to global viewership — a fundamental shift in how Netflix approaches international content strategy.

---

### 📅 Insight 10 — January & December are Peak Months
**What:** Netflix adds the most content in January and December each year.

**Why it occurs:** December additions are driven by holiday season demand — subscribers want fresh content during Christmas and New Year breaks. January additions follow the same logic — people make "watch more movies" part of their new year habits, and Netflix capitalizes on this by front-loading content.

**Business impact:** Content creators and distributors who want maximum visibility should negotiate January or December release dates with Netflix. Releases in slow months (March, September) get buried under less viewer attention.

---

### 📆 Insight 11 — 2010s Decade Has the Most Content
**What:** The 2010s produced more Netflix-available content than any other decade.

**Why it occurs:** The 2010s coincided with Netflix's global streaming expansion. The platform went from a US-only service to operating in 190+ countries between 2010–2019. This triggered a massive content acquisition spree, licensing movies and shows produced in the 2010s while also launching original productions.

**Business impact:** The dominance of 2010s content means older classics (1970s, 1980s) are underrepresented on Netflix. This is a strategic gap — platforms like HBO Max and Criterion Channel have seized this opportunity by focusing on classic cinema.

---

### 🔗 Insight 12 — Release Year & Added Year Have No Correlation (0.01)
**What:** The year a movie or show was released has almost no relationship with when it was added to Netflix.

**Why it occurs:** Netflix operates on a licensing model where availability depends on when rights become available, not when content was made. A 1995 film might get added in 2020 when its streaming rights are acquired, while a 2020 film might not appear until 2022 after its theatrical window closes.

**Business impact:** This explains why Netflix's library feels timeless — you can find content from any era. However, it also creates confusion for subscribers who expect new releases to appear quickly. Netflix addresses this with its "New on Netflix" feature to highlight recent additions regardless of release year.

---

### 🌏 Insight 13 — India vs USA vs Korea Content Comparison
**What:** USA leads in both Movies and TV Shows. India is strong in Movies but weak in TV Shows. Korea is strong in TV Shows (K-Dramas) but weaker in Movies.

**Why it occurs:** Each country's entertainment culture shapes its output. India's film industry (Bollywood) is one of the world's largest movie producers but TV drama culture is less developed for streaming. Korea excels in serialized drama storytelling, making TV Shows their dominant format.

**Business impact:** Netflix tailors its content investment per region — it funds more TV Show originals in Korea and more movie acquisitions in India. Understanding these cultural content patterns helps Netflix allocate its $17B annual content budget efficiently.

---

### 📈 Insight 14 — Genre Trends Over Years (2015–2021)
**What:** Drama consistently grew as the top genre from 2015 to 2021. International Movies and Comedies also grew significantly.

**Why it occurs:** Netflix's algorithm actively promotes content that keeps users watching longer. Dramas with multi-episode story arcs create "binge-watching" behavior better than any other genre. As Netflix understood this pattern, it deliberately commissioned more drama content.

**Business impact:** The rise of International Movies as a genre reflects Netflix's global strategy paying off. Content from India, Korea, Spain, and Brazil is now a significant portion of the library — reducing Netflix's dependence on expensive Hollywood content.

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

Made with ❤️ by **[Your Name]**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/muhammad-shayan-a20a433b8?utm_source=share_via&utm_content=profile&utm_medium=member_android)
---

⭐ **If you found this project helpful, please give it a star!** ⭐