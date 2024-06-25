from crewai import Task
from textwrap import dedent

class MovieFinderTasks():
  def Find_movies(self, agent, genre, actors=None, actresses=None): 
    actors_list = ', '.join(actors) if actors else 'None specified'
    actresses_list = ', '.join(actresses) if actresses else 'None specified'
    print(genre, actors_list, actresses_list)
    
    return Task(description=dedent(f"""
        Your task is to identify the top 5 movies that match the user's preferences based on genre and optionally specified favorite actors and actresses. 
        Please ensure the movies are highly rated and well-regarded within their genre.

        Criteria for selection:
        - Interested genre: {genre}
        - Favorite actors: {actors_list}
        - Favorite actresses: {actresses_list}

        Steps to accomplish this task:
        1. Search for movies within the specified genre.
        2. Filter and prioritize movies featuring the specified favorite actors and actresses, if any.
        3. Ensure the movies selected have good reviews and high ratings.
        4. Provide a brief description and reasons for selecting each of the top 5 movies.
      """),
      agent=agent,
      expected_output="A list of the top 5 movies matching the specified criteria, each with a brief description and reason for selection."
)

  def Identify_the_streaming_service(self, agent, location):
    return Task(description=dedent(f"""
        Your task is to identify which streaming services offer the previously identified top 5 movies in the user's specified location.
        The goal is to provide the user with the most accessible and convenient options to watch these movies.

        Location for streaming service search: {location}

        Steps to accomplish this task:
        1. Identify and list the top 5 movies found in the previous task.
        2. Research and determine which streaming platforms have the rights to stream each of these movies in {location}.
        3. Verify the availability and any location-specific restrictions or requirements.
        4. Compile a list of streaming services for each movie, ensuring to include subscription details if available.
        5. Provide clear instructions or links on how the user can access these movies on the identified streaming services.
      """),
      agent=agent,
      expected_output="A list of streaming services for each of the top 5 movies, including availability, location-specific restrictions, and subscription details."

      )
