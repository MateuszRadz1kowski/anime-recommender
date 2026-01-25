import requests
import json
import time

def anilist_export_data(page_number):
    query = '''
    query ($page: Int) {
        Page (page: $page) {
            pageInfo {
                currentPage
                hasNextPage
                perPage
            }
            media {
                id
                idMal
                title { english }
                tags { id rank }
                seasonYear
                format
                isAdult
                genres
                popularity
                favourites
                meanScore
                recommendations {
                    nodes { mediaRecommendation { id } }
                }
            }
        }
    }
    '''
    variables = {'page': page_number}
    url = 'https://graphql.anilist.co'

    try:
        response = requests.post(url, json={'query': query, 'variables': variables})
        if response.status_code == 429:  # rate limit
            print(f"Rate limit hit on page {page_number}, sleeping 10s...")
            time.sleep(10)
            return anilist_export_data(page_number)
        res = response.json()
        if "errors" in res:
            print("GraphQL error:", res["errors"])
            return {"data": {"Page": {"media": [], "pageInfo": {"hasNextPage": False}}}}
        return res
    except Exception as e:
        print("Request error:", e)
        return {"data": {"Page": {"media": [], "pageInfo": {"hasNextPage": False}}}}

def anilist_pack_data_to_db(res):
    media_list = res.get('data', {}).get('Page', {}).get('media', [])
    result = []

    for anime in media_list:
        try:
            anime_id = anime.get('id')
            if anime_id is None:
                continue

            id_mal = anime.get('idMal')
            title_english = anime.get('title', {}).get('english')
            season_year = anime.get('seasonYear')
            format_ = anime.get('format')
            is_adult = anime.get('isAdult')
            genres = anime.get('genres') if anime.get('genres') else []
            tags = json.dumps(anime.get('tags', []))
            recommendations = [
                rec.get("mediaRecommendation", {}).get("id")
                for rec in anime.get("recommendations", {}).get("nodes", [])
                if rec and rec.get("mediaRecommendation")
            ] if anime.get("recommendations") else []

            popularity = anime.get('popularity')
            favourites = anime.get('favourites')
            mean_score = anime.get('meanScore')

            result.append((
                anime_id,
                id_mal,
                title_english,
                season_year,
                format_,
                is_adult,
                genres,
                tags,
                recommendations,
                popularity,
                favourites,
                mean_score
            ))
        except Exception as e:
            print(f"Skipping anime due to error: {e}")
            continue

    return result


# query
# User($name: String) {
#     User(name: $name) {
#     name
# id
# mediaListOptions
# {
#     scoreFormat
# }
# favourites
# {
#     anime
# {
#     nodes
# {
#     title
# {
#     english
# }
# id
#
# }
# }
# }
# }
# }