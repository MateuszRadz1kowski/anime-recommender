import math
from math import log1p

from backend.app.anime_profile.user_anime_completed import user_anime_completed
from backend.config.reccomender_values_settings import ANIME_PROFILE_GENRE_MODIFIER, mean_score_multiplier


def create_anime_profile(db_response,user_interests_profile):
    anime_profile = {}
    anime_completed = user_anime_completed()
    for anime in db_response:
        anime_name = anime[2]
        if anime_name not in anime_completed:
            for tag in anime[7]:
                tag_name = tag["name"]
                tag_rank = tag["rank"]
                if tag_name in user_interests_profile[0]:
                    if anime_name not in anime_profile:
                        anime_profile[anime_name] = 0
                    else:
                        anime_profile[anime_name] += tag_rank * user_interests_profile[0].get(tag_name)
            for genre in anime[6]:
                if genre in user_interests_profile[1]:
                    if anime_name not in anime_profile:
                        anime_profile[anime_name] = 0
                    else:
                        anime_profile[anime_name] += ANIME_PROFILE_GENRE_MODIFIER * user_interests_profile[1].get(genre)
            anime_profile[anime_name] = anime_profile[anime_name] * mean_score_multiplier(anime[11]) * log1p(anime[10])
        else:
            continue
    normalise_score(anime_profile)

    sorted_anime_profile = sorted(
            anime_profile.items(),
            key=lambda x: x[1],
            reverse=True
        )
    print(sorted_anime_profile)

def normalise_score(anime):
    sum_sq = 0.0

    for value in anime.values():
        sum_sq += value ** 2

    norm = math.sqrt(sum_sq)

    for key in anime:
        anime[key] = anime[key] / norm

    return anime