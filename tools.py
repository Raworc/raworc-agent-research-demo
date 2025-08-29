from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

def get_research_tools():
    """Return a list of tools for the research agent"""
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    return [wikipedia]
