from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from backend.app.anime_profile.final_reccomendations_dict import prepare_dictionary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recommendations_data/")
async def get_recommendations(
    show_sequels: bool = Query(True),
    experimental_mode: bool = Query(False),
    show_18_rated: bool = Query(True),

    tag_importance: str = Query("medium"),
    popularity_importance: str = Query("medium"),

    min_number_episodes: int = Query(1, ge=1),
    max_number_episodes: int = Query(9999),

    min_release_year: int = Query(1900),
    max_release_year: int = Query(datetime.now().year),

    min_mean_score: int = Query(0),

    studios: Optional[List[str]] = Query(None),
    tags: Optional[List[str]] = Query(None),
    genres: Optional[List[str]] = Query(None),

    media_types: Optional[List[str]] = Query(["Anime", "Movie", "OVA"])
):
    data = prepare_dictionary()

    return data
# by uruchomic w folderze anime-recommender: python -m uvicorn backend.app.api.main:app --reload
#dane sa w: http://127.0.0.1:8000/recommendations_data