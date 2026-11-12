# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeMatch 1.0 — a small, rule-based music recommender.

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

VibeMatch ranks songs from a small catalog based on a user’s favorite genre, favorite mood, and target energy level. It is intended for classroom exploration of how preferences and scoring rules can produce recommendations. It assumes that genre, mood, and energy are useful clues about what a listener wants.

This project is not intended for real-world music recommendations or commercial use. It does not learn from listening history, likes, skips, or other user behavior.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The recommender compares each song’s genre and mood with the user’s preferences. A genre match adds 1 point, and a mood match adds 1 point. Energy similarity is calculated as 1 - the difference between the user’s target energy and the song’s energy, then multiplied by 2. The system adds these points, sorts songs from highest score to lowest, and returns the top five with reasons for their scores.

The first scoring version gave genre matches 2 points and energy similarity up to 1 point. In my experiment, I reduced the genre weight to 1 and doubled the energy weight to 2. This made energy similarity more influential in the rankings. The starter code returned the first songs in the catalog; my version loads and scores the songs before ranking them.

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog contains 15 songs: the original 10 plus 5 additional songs. Each row includes an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

The 12 genres represented are pop, lofi, rock, ambient, jazz, synthwave, indie pop, country, classical, reggae, R&B, and metal. The 9 moods are happy, chill, intense, relaxed, moody, focused, hopeful, peaceful, and romantic.

This is a small sample catalog. Lofi has three songs, pop has two, and each other genre has one. The recommender currently uses only genre, mood, and energy; it does not score tempo, valence, danceability, or acousticness.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The recommendations respond to the selected profile in an understandable way. The High-Energy Pop profile ranked “Sunrise City” first, Chill Lofi ranked “Library Rain” first, and Intense Rock ranked “Storm Runner” first. Each result includes reasons that show which preferences contributed to its score.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The catalog is small and unevenly distributed, so users who prefer a genre with only one song have little choice. Genres and moods must match exactly; the system does not know, for example, whether two different genres or mood labels are musically related.

The scoring ignores tempo, valence, danceability, acousticness, listening history, lyrics, and popularity. The likes_acoustic field in the starter UserProfile class is not used by the current scoring rule. A small catalog and limited features can produce narrow recommendations, and changing the weights can favor one preference over another.

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tried three profiles: High-Energy Pop, Chill Lofi, and Intense Rock. With the experimental weights, their top recommendations were:

High-Energy Pop: “Sunrise City” (3.84), “Gym Hero” (2.94), and “Rooftop Lights” (2.72).

Chill Lofi: “Library Rain” (3.90), “Midnight Coding” (3.76), and “Spacewalk Thoughts” (2.96).

Intense Rock: “Storm Runner” (3.98), “Gym Hero” (2.94), and “Iron Skies” (2.88).

I compared the original scoring weights with the experiment. For Chill Lofi, “Focus Flow” was third and “Spacewalk Thoughts” fourth with the original weights. After increasing the energy weight and lowering the genre weight, “Spacewalk Thoughts” moved to third and “Focus Flow” to fourth. Their closer energy match mattered more in the experiment. The top-ranked song remained the same for all three profiles.

The CLI displayed the song scores and explanations. I also ran the existing test suite with python -m pytest; both tests passed.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Add more songs and balance the catalog across genres and moods.
Use additional features such as tempo, valence, danceability, or acousticness.
Add user feedback and a diversity rule so recommendations do not keep favoring very similar songs.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

My biggest learning moment was seeing that a recommender’s rankings come directly from its scoring rules. Changing the genre and energy weights changed the order for the Chill Lofi profile, even though the catalog stayed the same. That helped me see how simple choices in an algorithm can affect what users discover.

AI helped me plan and implement the scoring logic, but I checked the output by comparing the printed explanations and scores with the formula. I also ran the program and the existing tests. I was surprised that a small rule-based system could feel like a real recommendation when it ranked songs by a few recognizable preferences. If I extended the project, I would add more balanced data, use more song features, and include a way to encourage variety.