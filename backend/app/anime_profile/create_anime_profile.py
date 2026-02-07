import math
from backend.app.anime_profile.check_filters import check_if_adult, check_format, check_season_year, check_show_planning
from backend.app.anime_profile.user_anime_status import user_anime_status
from backend.config.reccomender_values_settings import ANIME_PROFILE_GENRE_MODIFIER, mean_score_multiplier, \
    anime_favourites_multiplier, ANIME_USER_PLANNING_MULTIPLIER, ANIME_PROFILE_API_RECOMMENDATIONS_MODIFIER


def create_anime_profile(db_response,user_interests_profile):
    anime_profile = {}
    anime_completed = user_anime_status(0)
    anime_planning = user_anime_status(2)
    for anime in db_response:
        anime_name = anime[2]
        anime_score = 0
        if anime_name in anime_completed:
            continue

        if not (check_if_adult(anime) and check_format(anime) and check_season_year(anime) and check_show_planning(anime, anime_planning)):continue

        for tag in anime[7]:
            tag_name = tag["name"]
            tag_rank = tag["rank"]
            if tag_name in user_interests_profile[0]:
                if anime_name not in anime_profile:
                    anime_profile[anime_name] = 0
                else:
                    anime_score += tag_rank * user_interests_profile[0][tag_name]

        for genre in anime[6]:
            if genre in user_interests_profile[1]:
                if anime_name not in anime_profile:
                    anime_profile[anime_name] = 0
                else:
                    anime_score += ANIME_PROFILE_GENRE_MODIFIER * user_interests_profile[1][genre]

        if anime_name in anime_planning:
            anime_score *= ANIME_USER_PLANNING_MULTIPLIER

        if anime_name in user_interests_profile[2]:
            anime_score += ANIME_PROFILE_API_RECOMMENDATIONS_MODIFIER * user_interests_profile[2][anime_name]

        anime_score * mean_score_multiplier(anime[11])
        anime_score * anime_favourites_multiplier(anime[10])

        anime_profile[anime_name] = anime_score

    normalise_score(anime_profile)

    sorted_anime_profile = sorted(
            anime_profile.items(),
            key=lambda x: x[1],
            reverse=True
        )
    return sorted_anime_profile

def normalise_score(anime):
    sum_sq = 0.0

    for value in anime.values():
        sum_sq += value ** 2

    norm = math.sqrt(sum_sq)

    for key in anime:
        anime[key] = anime[key] / norm

    return anime