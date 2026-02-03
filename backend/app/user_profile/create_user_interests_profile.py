import math

from backend.app.user_profile.create_user_tag_profile import user_tag_profile
from backend.app.user_profile.user_genre_profile import user_genre_profile
from backend.scripts.tag_count import export_tag_count, get_tag_popularity_weight
from get_user_data import get_user_data
from backend.config.reccomender_values_settings import (REPEAT_MULTIPLIER, USER_FAVOURITES_MULTIPLIER, score_multiplier)

def create_user_interests_profile():
    data = get_user_data()
    entries = data['data']['MediaListCollection']['lists'][0]['entries']
    user_data = data['data']['User']

    user_tags = {}
    user_genres = {}

    for entry in entries:
        user_tag_profile(entry, user_data, user_tags)
        user_genre_profile(entry, user_data, user_genres)

    user_tags = normalise_score(user_tags)
    user_genres = normalise_score(user_genres)

    user_tags = sort_interests(user_tags)
    user_genres = sort_interests(user_genres)

    print(user_tags)
    print(user_genres)


def normalise_score(user_interests):
    sum_sq = 0.0

    for value in user_interests.values():
        sum_sq += value ** 2

    norm = math.sqrt(sum_sq)

    for key in user_interests:
        user_interests[key] = user_interests[key] / norm

    return user_interests


def sort_interests(user_interests):
    return dict(
        sorted(
            user_interests.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

create_user_interests_profile()


