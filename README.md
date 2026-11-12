# 🎵 Music Recommender Simulation: VibeMatch 1.0

## Project Summary

VibeMatch is a small, rule-based music recommender. It loads songs from a CSV file, compares each song with a user’s genre, mood, and energy preferences, then returns the highest-scoring songs with explanations.

## How The System Works

Real-world recommenders can use collaborative filtering, which learns from patterns in user behavior, and content-based filtering, which compares item features with a user’s preferences. This simulation uses the content-based approach: it compares song attributes with preferences in a user profile.

Each song includes a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The scoring rule currently uses genre, mood, and energy. A genre match earns 1 point, a mood match earns 1 point, and energy similarity earns up to 2 points:

```text
energy similarity = 1 - |target energy - song energy|
score = genre points + mood points + (2 × energy similarity)
```

The program scores every song, sorts the results from highest to lowest, and returns the top five. It also prints the reasons for each score. The `UserProfile` class includes a `likes_acoustic` field, but the current scoring rule does not use it.

## Getting Started

Run commands from the project’s root folder.

```bash
python -m src.main
```

Run the existing tests with:

```bash
python -m pytest
```

## Sample Recommendation Output

The following is the actual CLI output with the experimental weights: genre = 1 point, mood = 1 point, and energy similarity = up to 2 points.

### High-Energy Pop

```text
High-Energy Pop recommendations:

Sunrise City - Score: 3.84
Because: genre match (+1.0); mood match (+1.0); energy similarity (+1.84)

Gym Hero - Score: 2.94
Because: genre match (+1.0); energy similarity (+1.94)

Rooftop Lights - Score: 2.72
Because: mood match (+1.0); energy similarity (+1.72)

Storm Runner - Score: 1.98
Because: energy similarity (+1.98)

Iron Skies - Score: 1.88
Because: energy similarity (+1.88)
```

### Chill Lofi

```text
Chill Lofi recommendations:

Library Rain - Score: 3.90
Because: genre match (+1.0); mood match (+1.0); energy similarity (+1.90)

Midnight Coding - Score: 3.76
Because: genre match (+1.0); mood match (+1.0); energy similarity (+1.76)

Spacewalk Thoughts - Score: 2.96
Because: mood match (+1.0); energy similarity (+1.96)

Focus Flow - Score: 2.80
Because: genre match (+1.0); energy similarity (+1.80)

Coffee Shop Stories - Score: 1.86
Because: energy similarity (+1.86)
```

### Intense Rock

```text
Intense Rock recommendations:

Storm Runner - Score: 3.98
Because: genre match (+1.0); mood match (+1.0); energy similarity (+1.98)

Gym Hero - Score: 2.94
Because: mood match (+1.0); energy similarity (+1.94)

Iron Skies - Score: 2.88
Because: mood match (+1.0); energy similarity (+1.88)

Sunrise City - Score: 1.84
Because: energy similarity (+1.84)

Rooftop Lights - Score: 1.72
Because: energy similarity (+1.72)
```

## Experiments You Tried

The original scoring rule gave genre matches 2 points, mood matches 1 point, and energy similarity up to 1 point. I changed the weights by reducing genre to 1 point and doubling the energy contribution to a maximum of 2 points.

For the Chill Lofi profile, “Focus Flow” ranked third and “Spacewalk Thoughts” fourth with the original weights. After the change, “Spacewalk Thoughts” moved to third and “Focus Flow” to fourth because its energy was closer to the user’s target. The top-ranked song stayed the same for all three profiles. This showed that feature weights can change the middle of a ranking even when the strongest match remains on top.

## Limitations and Risks

The catalog contains only 15 songs and is unevenly distributed: it has three lofi songs, two pop songs, and one song for each other genre. A user whose genre is missing, or represented by only one song, will receive limited choices.

Genre and mood matches require exact text matches. The system does not understand musical similarity, lyrics, user listening history, popularity, or whether a song is culturally appropriate for a listener. It also ignores tempo, valence, danceability, and acousticness when scoring. These limits can make recommendations narrow or repetitive.

## Reflection

This exercise helped me see that recommendations come from the data and scoring rules a system uses. Changing the genre and energy weights changed the Chill Lofi ranking, even though the songs stayed the same. AI helped me develop and explain the code, and I checked its output against the scoring formula and ran the existing tests. I was surprised that a simple rule-based system could still produce recommendations that felt personalized. If I continued the project, I would add a larger, more balanced catalog, use more song features, and give users a way to provide feedback.