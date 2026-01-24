import psycopg2
import time
from config import load_config
from anilist_export_data import anilist_export_data, anilist_pack_data_to_db

INSERT_SQL = """
INSERT INTO anime_data (
    id,
    id_mal,
    title_english,
    season_year,
    format,
    is_adult,
    genres,
    tags,
    recommendations,
    popularity,
    favourites,
    mean_score
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (id) DO NOTHING
"""

def insert_anime_data(config, data):
    if not data:
        return
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(INSERT_SQL, data)
            conn.commit()
            print(f"Inserted {len(data)} records")
    except Exception as e:
        print("DB ERROR:", e)

config = load_config()
page = 1

while True:
    print(f"Fetching page {page}...")
    anime_data = anilist_export_data(page)
    anime_data_packed = anilist_pack_data_to_db(anime_data)

    if anime_data_packed:
        insert_anime_data(config, anime_data_packed)
    else:
        print(f"No media found on page {page}, skipping.")

    has_next = anime_data.get("data", {}).get("Page", {}).get("pageInfo", {}).get("hasNextPage", False)
    if not has_next:
        print("All pages fetched.")
        break

    page += 1
