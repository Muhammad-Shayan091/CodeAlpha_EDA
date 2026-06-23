# ============================================================
# NETFLIX EDA PROJECT
# Libraries used: pandas & numpy ONLY (for data work)
# matplotlib is used ONLY for charts — no data logic in it
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# ===================
# STEP 1: LOAD DATA
# ===================
df = pd.read_csv('netflix_titles.csv')

print("=" * 55)
print("STEP 1: DATA LOADED")
print("=" * 55)

# ======================
# NO OF ROWS AND COLUMNS
# ======================
print(f"Rows    : {df.shape[0]}")                      
print(f"Columns : {df.shape[1]}")                       

# ============================
# LIST OF COLUMNS IN THE DATA
# ============================
print(f"\nColumn Names:\n{df.columns.tolist()}")

# =======================
# PRINTING FIRST "n" ROWS
# =======================
print(f"\nFirst 3 rows:")
print(df.head(3))


# ======================
# STEP 2: DATA OVERVIEW
# ======================
print("\n" + "=" * 55)
print("STEP 2: DATA OVERVIEW")
print("=" * 55)
print(df.dtypes)
missing = df.isnull().sum()
missing_pct = np.round((missing / len(df)) * 100, 2)

# pd.DataFrame() builds a new table from a dictionary
missing_table = pd.DataFrame({
    'Missing Count': missing,
    'Missing %'    : missing_pct
})

print("\nMissing Values Per Column:")
print(missing_table[missing_table['Missing Count'] > 0])

# =====================
# STEP 3: DATA CLEANING
# =====================
print("\n" + "=" * 55)
print("STEP 3: DATA CLEANING")
print("=" * 55)

# FILL MISSING TEXT WITH PLACEHOLDER
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)

# CHECKING DUPLICATES VALUES
dupes = df.duplicated().sum()   
print(f"Duplicate rows found: {dupes}")
df.drop_duplicates(inplace=True)

# CONVERT TEXT TO REAL-DATE
df['date_added'] = df['date_added'].str.strip()
df['date_added_parsed'] = pd.to_datetime(df['date_added'], errors='coerce')

# PULL (YEAR , MONTH , DAY) FROM THE REAL_DATE 
df['year_added']  = df['date_added_parsed'].dt.year
df['year_added'] = df['year_added'].fillna(0).astype(int)

# print("Cleaning done!")
print(f"Remaining rows after cleaning: {len(df)}")

# ================================================
# STEP 4: CONTENT TYPE ANALYSIS MOVIES VS TV SHOWS
# ================================================
print("\n" + "=" * 55)
print("STEP 4: CONTENT TYPE (Movie vs TV Show)")
print("=" * 55)
type_counts = df['type'].value_counts()
print(type_counts)

# PERCENTAGE BY CATEGORIES (Movies & TV Shows)
type_pct = np.round(type_counts / len(df) * 100, 1)
print("\nPercentage:")
print(type_pct)

# CHART BY MATPLOTLIB 
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(type_counts.index, type_counts.values, color=["#15b400", '#ff7f0e'])
ax.set_title('Movies vs TV Shows on Netflix', fontsize=14, fontweight='bold')
ax.set_ylabel('Count')
for i, v in enumerate(type_counts.values):
    ax.text(i, v + 20, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('01_content_type.png', dpi=150)
plt.show()
print("Saved: 01_content_type.png")

# ==============================
# STEP 5: CONTENT ADDED PER YEAR
# ==============================
print("\n" + "=" * 55)
print("STEP 5: CONTENT ADDED PER YEAR")
print("=" * 55)

yearly = (
    df.groupby(['year_added', 'type'])
    .size()
    .unstack(fill_value=0)   # fill_value=0 means no NaN, put 0
    .sort_index()
)
print(yearly)

# CHART FOR THE CATEGORIES (MOVIES & TV SHOWS) BY YEAR'S
yearly.plot(kind='bar', color=["#EE2D2D", "#1a6c72"], figsize=(13, 6))
plt.title('Content Added to Netflix Per Year', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('02_content_per_year.png', dpi=150)
plt.show()
print("Saved: 02_content_per_year.png")


# =====================
# STEP 6: TOP COUNTRIES
# =====================
print("\n" + "=" * 55)
print("STEP 6: TOP CONTENT-PRODUCING COUNTRIES")
print("=" * 55)

# TAKES ONLY THE FIRST COUNTRY
df['primary_country'] = df['country'].str.split(',').str[0].str.strip()

# RANK THE FREQUENCY AND FIND TOP COUNTRIES 
top_countries = df['primary_country'].value_counts().head(15)
print(top_countries)

# CHART TO SHOW THE TOP COUNTRIES
fig, ax = plt.subplots(figsize=(13, 7))
ax.barh(top_countries.index[::-1], top_countries.values[::-1], color='#E50914')
ax.set_title('Top 15 Countries on Netflix', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Titles')
for i, v in enumerate(top_countries.values[::-1]):
    ax.text(v + 2, i, str(v), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('03_top_countries.png', dpi=150)
plt.show()
print("Saved: 03_top_countries.png")

# ============================
# STEP 7: RATINGS DISTRIBUTION
# ============================
print("\n" + "=" * 55)
print("STEP 7: RATINGS DISTRIBUTION")
print("=" * 55)

ratings = df['rating'].value_counts().head(12)
print(ratings)

fig, ax = plt.subplots(figsize=(13, 6))
ax.bar(ratings.index, ratings.values, color='#E50914', edgecolor='white')
ax.set_title('Content Ratings on Netflix', fontsize=14, fontweight='bold')
ax.set_xlabel('Rating')
ax.set_ylabel('Count')
plt.xticks(rotation=45)
for i, v in enumerate(ratings.values):
    ax.text(i, v + 5, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('04_ratings.png', dpi=150)
plt.show()
print("Saved: 04_ratings.png")


# ==================
# STEP 8: TOP GENRES
# ==================
print("\n" + "=" * 55)
print("STEP 8: TOP GENRES")
print("=" * 55)

# explode() is a powerful pandas function:
# "Dramas, Comedies" in one row becomes two separate rows
all_genres = df['listed_in'].str.split(', ').explode()
top_genres = all_genres.value_counts().head(15)
print(top_genres)

fig, ax = plt.subplots(figsize=(13, 7))
ax.barh(top_genres.index[::-1], top_genres.values[::-1], color='#E50914')
ax.set_title('Top 15 Genres on Netflix', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Titles')
for i, v in enumerate(top_genres.values[::-1]):
    ax.text(v + 2, i, str(v), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('05_top_genres.png', dpi=150)
plt.show()
print("Saved: 05_top_genres.png")


# ======================
# STEP 9: MOVIE DURATION
# ======================
print("\n" + "=" * 55)
print("STEP 9: MOVIE DURATION ANALYSIS")
print("=" * 55)

# FILTER ONLY MOVIES USING BOOLEAN INDEXING
movies = df[df['type'] == 'Movie'].copy()

# REMOVE MIN TEXT -> CONVERT TO NUMBER 
movies['duration_min'] = (
    movies['duration']
    .str.replace(' min', '', regex=False)
)
movies['duration_min'] = pd.to_numeric(movies['duration_min'], errors='coerce')

# DROP ROWS WHERE DURATION COULD NOT BE PARSED
dur = movies['duration_min'].dropna()

# NUMPY FOR THE STATS
print(f"Total Movies  : {len(dur)}")
print(f"Minimum       : {np.min(dur):.0f} min")
print(f"Maximum       : {np.max(dur):.0f} min")
print(f"Mean (Average): {np.mean(dur):.0f} min")
print(f"Median        : {np.median(dur):.0f} min")
print(f"Std Deviation : {np.std(dur):.0f} min")
print(f"25th Percentile: {np.percentile(dur, 25):.0f} min")
print(f"75th Percentile: {np.percentile(dur, 75):.0f} min")

fig, ax = plt.subplots(figsize=(13, 6))
ax.hist(dur, bins=40, color='#E50914', edgecolor='white')
ax.axvline(np.mean(dur), color='yellow', linestyle='--', linewidth=2,
           label=f'Mean: {np.mean(dur):.0f} min')
ax.set_title('Movie Duration Distribution', fontsize=14, fontweight='bold')
ax.set_xlabel('Duration (minutes)')
ax.set_ylabel('Number of Movies')
ax.legend()
plt.tight_layout()
plt.savefig('06_movie_duration.png', dpi=150)
plt.show()
print("Saved: 06_movie_duration.png")


# ========================
# STEP 10: TV SHOW SEASONS
# ========================
print("\n" + "=" * 55)
print("STEP 10: TV SHOW SEASONS")
print("=" * 55)

shows = df[df['type'] == 'TV Show'].copy()

# "1 Season" → "1", "2 Seasons" → "2"
shows['seasons'] = (
    shows['duration']
    .str.replace(' Seasons', '', regex=False)
    .str.replace(' Season', '', regex=False)
)
shows['seasons'] = pd.to_numeric(shows['seasons'], errors='coerce')

season_counts = shows['seasons'].value_counts().sort_index()
print(season_counts)

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(season_counts.index.astype(int), season_counts.values, color='#E50914', edgecolor='white')
ax.set_title('TV Shows by Number of Seasons', fontsize=14, fontweight='bold')
ax.set_xlabel('Seasons')
ax.set_ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('07_tv_seasons.png', dpi=150)
plt.show()
print("Saved: 07_tv_seasons.png")

# ======================
# STEP 11: TOP DIRECTORS
# ======================
print("\n" + "=" * 55)
print("STEP 11: TOP DIRECTORS")
print("=" * 55)

top_directors = (
    df[df['director'] != 'Unknown']['director']
    .value_counts()
    .head(10)
)
# ORINT THE TOP DIRECTORS BY CHART

fig, ax = plt.subplots(figsize=(13, 6))
ax.barh(top_directors.index[::-1], top_directors.values[::-1], color='#E50914')
ax.set_title('Top 10 Directors on Netflix', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Titles')
for i, v in enumerate(top_directors.values[::-1]):
    ax.text(v + 0.1, i, str(v), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('08_top_directors.png', dpi=150)
plt.show()
print("Saved: 08_top_directors.png")


# ==================================
# STEP 12: MONTHLY CONTENT ADDITIONS
# ==================================
print("\n" + "=" * 55)
print("STEP 12: MONTHLY CONTENT ADDITIONS")
print("=" * 55)

df["date_added_parsed"] = pd.to_datetime(df['date_added'] , format='mixed' , errors='coerce')
df['month_added'] = df['date_added_parsed'].dt.month
month_map = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',
             7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

monthly = (
    df.dropna(subset=["month_added"])
    .groupby("month_added")
    .size()                        # count rows per month
    .reset_index(name='count')     # rename the count column
)
# REPLACE EACH NUMBER WITH IT'S MONTH NAME
monthly['month_name'] = monthly['month_added'].map(month_map)
print(monthly[['month_name', 'count']])

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly['month_name'], monthly['count'],
        marker='o', color='#E50914', linewidth=2.5)
ax.fill_between(monthly['month_name'], monthly['count'], alpha=0.2, color='#E50914')
ax.set_title('Titles Added to Netflix by Month', fontsize=14, fontweight='bold')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Titles Added')
plt.tight_layout()
plt.savefig('09_monthly_additions.png', dpi=150)
plt.show()
print("Saved: 09_monthly_additions.png")

# ===========================
# STEP 13: RELEASE YEAR TREND
# ===========================
print("\n" + "=" * 55)
print("STEP 13: RELEASE YEAR TREND")
print("=" * 55)

release_trend = (
    df.groupby('release_year')
    .size()
    .reset_index(name='count')
    .sort_values('release_year')
)
print(release_trend.tail(15))   # show last 15 years

# numpy to find peak year
peak_idx = np.argmax(release_trend['count'].values)
peak_year = release_trend.iloc[peak_idx]['release_year']
print(f"\nPeak release year: {int(peak_year)}")

fig, ax = plt.subplots(figsize=(13, 6))
ax.plot(release_trend['release_year'], release_trend['count'],
        color='#E50914', linewidth=2)
ax.fill_between(release_trend["release_year"],release_trend["count"], alpha = 0.3 , color = "#E50914")
ax.set_title('Number of Titles by Release Year', fontsize=14, fontweight='bold')
ax.set_xlabel('Release Year')
ax.set_ylabel('Number of Titles')
plt.tight_layout()
plt.savefig('10_release_year.png', dpi=150)
plt.show()
print("Saved: 10_release_year.png")


# ============================
# STEP 14: CORRELATION (numpy)
# ============================
print("\n" + "=" * 55)
print("STEP 14: CORRELATION ANALYSIS (numpy)")
print("=" * 55)

# DROP ROWS WITH ANY NAN IN THESE COLUMNS
num_df = df[['release_year', 'year_added']].dropna()

# # CONVERT TO NUMPY ARRAYS
arr = num_df.values.T   
corr_matrix = np.corrcoef(arr)

# Build a pandas DataFrame for clean display
corr_df = pd.DataFrame(
    np.round(corr_matrix, 3),
    index=num_df.columns,
    columns=num_df.columns
)
print("\nCorrelation Matrix:")
print(corr_df)

fig, ax = plt.subplots(figsize=(7, 5))
im = ax.imshow(corr_matrix, cmap='Reds', vmin=-1, vmax=1)
ax.set_xticks(range(2))
ax.set_yticks(range(2))
ax.set_xticklabels(num_df.columns, rotation=30)
ax.set_yticklabels(num_df.columns)
for i in range(2):
    for j in range(2):
        ax.text(j, i, f"{corr_matrix[i,j]:.2f}", ha='center', va='center',
                fontweight='bold', color='black')
plt.colorbar(im, ax=ax)
ax.set_title('Correlation Heatmap', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('11_correlation.png', dpi=150)
plt.show()
print("Saved: 11_correlation.png")


# ============================
# STEP 15: TOP ACTORS ANALYSIS
# ============================
print("\n" + "=" * 55)
print("STEP 16: TOP ACTORS ANALYSIS")
print("=" * 55)

# REMOVE UNKNOWN CAST AND THEN SPLIT
all_actors = (
    df[df['cast'] != 'Unknown']['cast']
    .str.split(', ')
    .explode()
    .str.strip()
)

top_actors = all_actors.value_counts().head(10)
print(top_actors)

fig, ax = plt.subplots(figsize=(13, 7))
ax.barh(top_actors.index[::-1], top_actors.values[::-1], color='#E50914', edgecolor='white')
ax.set_title('Top 10 Actors on Netflix', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Titles')
for i, v in enumerate(top_actors.values[::-1]):
    ax.text(v + 0.1, i, str(v), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('12_top_actors.png', dpi=150)
plt.show()
print("Saved: 12_top_actors.png")


# =========================================
# STEP 16: INDIA vs USA vs KOREA COMPARISON
# =========================================
print("\n" + "=" * 55)
print("STEP 17: INDIA vs USA vs KOREA COMPARISON")
print("=" * 55)


df['primary_country'] = df['country'].str.split(',').str[0].str.strip()
countries = ['United States', 'India', 'South Korea']
filtered = df[df['primary_country'].isin(countries)]

# Movies aur TV Shows dono count
comparison = (
    filtered.groupby(['primary_country', 'type'])
    .size()
    .unstack(fill_value=0)
    .sort_values('Movie', ascending=False)
)
print(comparison)

# Chart
comparison.plot(kind='bar', color=['#E50914', '#564d4d'],
                figsize=(10, 6), edgecolor='white')
plt.title('India vs USA vs Korea — Movies & TV Shows',
          fontsize=14, fontweight='bold')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=0)
plt.legend(title='Type')
plt.tight_layout()
plt.savefig('13_country_comparison.png', dpi=150)
plt.show()
print("Saved: 13_country_comparison.png")


# ============================================================
# STEP 17: GENRE TREND OVER YEARS
# ============================================================
print("\n" + "=" * 55)
print("STEP 18: GENRE TREND OVER YEARS")
print("=" * 55)

# TOP 5 GENRES
all_genres = df['listed_in'].str.split(', ').explode()
top5_genres = all_genres.value_counts().head(5).index.tolist()

df_exploded = df.dropna(subset=['year_added']).copy()
df_exploded['year_added'] = df_exploded['year_added'].astype(int)
df_exploded['genre'] = df_exploded['listed_in'].str.split(', ')
df_exploded = df_exploded.explode('genre')

genre_year = (
    df_exploded[df_exploded['genre'].isin(top5_genres)]
    .groupby(['year_added', 'genre'])
    .size()
    .unstack(fill_value=0)
)
print(genre_year)
genre_year = genre_year[genre_year.index >= 2015]
genre_year.plot(figsize=(14, 7), marker='o', linewidth=2)
plt.title('Top 5 Genre Trends Over Years', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.legend(title='Genre')
plt.tight_layout()
plt.savefig('14_genre_trends.png', dpi=150)
plt.show()
print("Saved: 14_genre_trends.png")

# ======================================
# STEP 18: BEST MONTH TO RELEASE CONTENT
# ======================================
print("\n" + "=" * 55)
print("STEP 19: BEST MONTH TO RELEASE CONTENT")
print("=" * 55)

month_map = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May',
             6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct',
             11:'Nov', 12:'Dec'}

df['date_added_parsed'] = pd.to_datetime(df['date_added'], format='mixed', errors='coerce')
df['month_added'] = df['date_added_parsed'].dt.month

monthly = (
    df.dropna(subset=['month_added'])
    .groupby('month_added')
    .size()
    .reset_index(name='count')
)
monthly['month_name'] = monthly['month_added'].map(month_map)

best_month = monthly.loc[monthly['count'].idxmax(), 'month_name']
print(f"Best month to add content: {best_month}")
print(monthly[['month_name', 'count']])

fig, ax = plt.subplots(figsize=(13, 6))
ax.bar(monthly['month_name'], monthly['count'],
       color='#E50914', edgecolor='white')
ax.set_title('Best Month to Add Content on Netflix',
             fontsize=14, fontweight='bold')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Titles Added')
ax.axhline(monthly['count'].mean(), color='yellow',
           linestyle='--', linewidth=2, label='Average')
ax.legend()
plt.tight_layout()
plt.savefig('15_best_month.png', dpi=150)
plt.show()
print(f"Saved: 15_best_month.png")


# ===========================
# STEP 19: CONTENT PER DECADE
# ===========================
print("\n" + "=" * 55)
print("STEP 20: CONTENT PER DECADE")
print("=" * 55)

# Decade column 
df['decade'] = (df['release_year'] // 10 * 10).astype(str) + 's'

decade_counts = (
    df.groupby(['decade', 'type'])
    .size()
    .unstack(fill_value=0)
    .sort_index()
)
print(decade_counts)
decade_counts = decade_counts[decade_counts.index >= '1950s']
decade_counts.plot(kind='bar', color=['#E50914', '#564d4d'],
                   figsize=(13, 6), edgecolor='white')
plt.title('Netflix Content Per Decade', fontsize=14, fontweight='bold')
plt.xlabel('Decade')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45)
plt.legend(title='Type')
plt.tight_layout()
plt.savefig('16_content_per_decade.png', dpi=150)
plt.show()
print("Saved: 16_content_per_decade.png")


# ======================
# STEP 20: FINAL SUMMARY
# ======================
print("\n" + "=" * 55)
print("STEP 15: FINAL INSIGHTS SUMMARY")
print("=" * 55)

total          = len(df)
n_movies       = df[df['type'] == 'Movie'].shape[0]
n_shows        = df[df['type'] == 'TV Show'].shape[0]
df["primary_country"] = df['country'].str.split(",").str[0].str.strip()
top_country    = df['primary_country'].value_counts().idxmax()
top_rating     = df['rating'].value_counts().idxmax()
all_genres = df["listed_in"].str.split(", ").explode()
top_genre      = all_genres.value_counts().idxmax()
peak_add_year  = int(df['year_added'].value_counts().idxmax())
movies = df[df['type'] == 'Movie'].copy()
movies["duration_min"] = pd.to_numeric(movies["duration"].str.replace(" min", "", regex=False), errors='coerce')
avg_dur        = int(np.mean(movies['duration_min'].dropna()))
all_actors = df[df['cast'] != 'Unknown']['cast'].str.split(', ').explode().str.strip()
month_map = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May',
             6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct',
             11:'Nov', 12:'Dec'}

df['date_added_parsed'] = pd.to_datetime(df['date_added'], format='mixed', errors='coerce')
df['month_added'] = df['date_added_parsed'].dt.month

monthly = (
    df.dropna(subset=['month_added'])
    .groupby('month_added')
    .size()
    .reset_index(name='count')
)
monthly['month_name'] = monthly['month_added'].map(month_map)
best_month = monthly.loc[monthly['count'].idxmax(), 'month_name']

print(f"""
🎬 NETFLIX EDA — FINAL SUMMARY
{'='*50}
Total Titles        : {total:,}
Movies              : {n_movies:,}  ({n_movies/total*100:.1f}%)
TV Shows            : {n_shows:,}  ({n_shows/total*100:.1f}%)
Top Country         : {top_country}
Most Common Rating  : {top_rating}
Most Common Genre   : {top_genre}
Peak Year (Added)   : {peak_add_year}
Avg Movie Duration  : {avg_dur} minutes
{'='*50}
📊 ADDITIONAL INSIGHTS
{'='*50}
🎭 Top Actor        : {all_actors.value_counts().idxmax()}
🇺🇸 USA Movies      : {len(df[(df['primary_country']=='United States') & (df['type']=='Movie')])}
🇮🇳 India Movies    : {len(df[(df['primary_country']=='India') & (df['type']=='Movie')])}
🇰🇷 Korea TV Shows  : {len(df[(df['primary_country']=='South Korea') & (df['type']=='TV Show')])}
📅 Best Month       : {best_month}
📆 Peak Decade      : {df['decade'].value_counts().idxmax()}
{'='*50}
""")