import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class Song:
    """Represent a song and its attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represent a user's music preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Recommend and explain songs for a user profile."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return songs ranked by the user's genre, mood, and energy preferences."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }

        scored_songs = []

        for song in self.songs:
            song_data = {
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
            }
            score, _ = score_song(user_prefs, song_data)
            scored_songs.append((song, score))

        ranked_songs = sorted(
            scored_songs,
            key=lambda result: result[1],
            reverse=True,
        )

        return [song for song, _ in ranked_songs[:max(k, 0)]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain how a song matched the user's preferences."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }
        song_data = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
        }

        _, reasons = score_song(user_prefs, song_data)
        return "; ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["tempo_bpm"] = float(row["tempo_bpm"])

            for field in ("energy", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])

            songs.append(row)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song using genre, mood, and energy preferences."""
    score = 0.0
    reasons = []

    if user_prefs["genre"].lower() == song["genre"].lower():
        score += 1.0
        reasons.append("genre match (+1.0)")

    if user_prefs["mood"].lower() == song["mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_similarity = max(
        0.0,
        1.0 - abs(user_prefs["energy"] - song["energy"]),
    )
    energy_points = 2.0 * energy_similarity
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by score, with explanations."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(
        scored_songs,
        key=lambda result: result[1],
        reverse=True,
    )

    return ranked_songs[:max(k, 0)]