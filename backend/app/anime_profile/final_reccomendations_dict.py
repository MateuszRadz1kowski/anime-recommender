from backend.app.anime_profile.create_anime_profile import create_anime_profile
from backend.app.db.get_data.get_anime_data_db import get_anime_data
from backend.app.user_profile.create_user_interests_profile import create_user_interests_profile


def prepare_dictionary():
    anime_data = get_anime_data()
    user_interests_profile = create_user_interests_profile()
    anime_reccomendations = create_anime_profile(anime_data, user_interests_profile)
    print(f"tag scores: {user_interests_profile[0]}")
    print(f"genre scores: {user_interests_profile[1]}")
    print(f"anime recommendations: {anime_reccomendations}")
prepare_dictionary()