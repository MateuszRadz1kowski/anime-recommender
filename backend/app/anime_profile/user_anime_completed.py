from backend.app.user_profile.get_user_data import get_user_data


def user_anime_completed():
    anime_completed = {}
    entries = get_user_data()['data']['MediaListCollection']['lists'][0]['entries']
    for entry in entries:
        entry_title = entry["media"]["title"]["english"]
        if entry_title not in anime_completed:
            anime_completed[entry_title] = entry_title
    return anime_completed
