from crewai import Crew
from textwrap import dedent
from movie_finder_agents import MovieAgents
from movie_finder_tasks import MovieFinderTasks
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

class MovieCrew:

    def __init__(self, genre, actors, actresses, location):
        self.genre = genre
        self.actors = actors
        self.actresses = actresses
        self.location = location

    @lru_cache(maxsize=128)  # Cache up to 128 different combinations
    def run(self):
        agents = MovieAgents(self.genre)
        tasks = MovieFinderTasks()

        movie_selector_agent = agents.movie_selection_agent()
        streamingservice_selector_agent = agents.streaming_services_agent()

        movie_identify_task = tasks.Find_movies(
            movie_selector_agent,
            self.genre,
            self.actors,
            self.actresses,
        )
        stremingservice_identify_task = tasks.Identify_the_streaming_service(
            streamingservice_selector_agent,
            self.location,
        )

        crew = Crew(
            agents=[
                movie_selector_agent, streamingservice_selector_agent,
            ],
            tasks=[movie_identify_task, stremingservice_identify_task],
            verbose=True
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    genre = None
    location = None

    while not genre:
        genre = input(dedent("""\
            In which genre are you interested? 
        """)).strip()
        if not genre:
            print("Genre is compulsory. Please enter a valid genre.")

    # Optional inputs
    actors = input(dedent("""\
            Who are your favorite actors? (optional) 
        """)).strip() or None
    actresses = input(dedent("""\
            Who are your favorite actresses? (optional) 
        """)).strip() or None

    while not location:
        location = input(dedent("""\
            Which country do you stay in? 
        """)).strip()
        if not location:
            print("Location is compulsory. Please enter a valid location.")

    # Ensure actors and actresses are in a hashable form for caching
    actors = tuple(actors.split(',')) if actors else None
    actresses = tuple(actresses.split(',')) if actresses else None

    movie_crew = MovieCrew(genre, actors, actresses, location)
    result = movie_crew.run()
    print("\n\n########################")
    print("## Here is your suggestion for movies")
    print("########################\n")
    print(result)
