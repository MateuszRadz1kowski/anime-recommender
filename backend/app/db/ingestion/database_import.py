import psycopg2

from backend.config.db_settings import HOST,DATABASE,USER,PASSWORD
from backend.scripts.tag_count import count_tags
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

def insert_anime_data(data):
    config = {'host': HOST, 'database': DATABASE, 'user': USER, 'password': PASSWORD}
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

page = 1

while True:
    print(f"Fetching page {page}...")
    anime_data = anilist_export_data(page)
    anime_data_packed = anilist_pack_data_to_db(anime_data)

    count_tags(anime_data_packed)
    insert_anime_data(anime_data_packed)

    has_next = anime_data.get("data", {}).get("Page", {}).get("pageInfo", {}).get("hasNextPage", False)
    if not has_next:
        print("All pages fetched.")
        break

    page += 1
