from crewai import Agent
from langchain.llms import OpenAI
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
import os
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")


llm = ChatCohere()
class MovieAgents():
  def __init__(self, genre_name):
        """
        Initializes the SearchTMDBMovies object with the provided genre name.

        Parameters:
            genre_name (str): The name of the genre for movie search.

        Returns:
            None
        """
        self.genre_name = genre_name


  def movie_selection_agent(self):
    """
    A function that returns an Agent object representing a Movie Selection Expert.

    Returns:
        Agent: An Agent object with the role, goal, backstory, tools, Verbose, and cache attributes set.
    """
    print('data passed')
    return Agent(
        role='Movie Selection Expert',
        goal='Select the top 5 movies based on genre, favorite actors, and favorite actresses',
        backstory='''
        You are a seasoned professional with over 15 years of experience in the film industry, specializing in curating personalized movie recommendations. 
        Your expertise lies in understanding diverse tastes and preferences, allowing you to recommend movies based on the user's preferred genre and optionally favored actors and actresses. 
        Staying updated with the latest industry trends and cinematic developments, you ensure that your recommendations are both popular and critically acclaimed. 
        Your role is to curate a list of the best movies tailored to the user's preferences. 
        You have access to advanced search tools and a comprehensive database of movie reviews and ratings to ensure your selections are top-notch.
        ''',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
            # SearchTMDBMovies(self.genre_name).get_movie_details_tool()
        ],
        Verbose = True,
        llm = llm,
        cache=True)

  def streaming_services_agent(self):
    """
    A function that returns an Agent object representing a Streaming Services Finding Expert.

    Returns:
        Agent: An Agent object with the role, goal, backstory, tools, and verbose attributes set.
    """
    return Agent(
        role='Streaming Services Finding Expert',
        goal='Identify available streaming services for the selected movies in the specified location and provide access details',
        backstory='''
        As a Streaming Services Finding Expert, you are highly specialized in researching and identifying streaming platforms. 
        With a decade of experience in the digital streaming landscape, your expertise lies in locating which services offer the selected movies in the user's specified location. 
        You excel in navigating various streaming services, understanding regional availability, and providing accurate access details. 
        By leveraging your deep knowledge of regional licensing agreements and constantly evolving streaming libraries, you ensure that users receive the most current and relevant information. 
        Your mission is to locate which services offer the recommended movies in the user's specified location and  provide clear, step-by-step instructions on how to access the desired films, making the viewing experience seamless and convenient for the user.
        ''',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True,
        llm = llm)
