from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain.tools import Tool
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper
import requests
from bs4 import BeautifulSoup
from typing import Optional
import time

def get_web_content(url: str) -> str:
    """
    Fetch and extract text content from a web page.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Limit text length
        return text[:3000] + "..." if len(text) > 3000 else text
        
    except Exception as e:
        return f"Error fetching content from {url}: {str(e)}"

def search_news(query: str) -> str:
    """
    Search for recent news articles related to the query.
    """
    try:
        # Use DuckDuckGo to search for recent news
        search_wrapper = DuckDuckGoSearchAPIWrapper(region="en-us", time="d", max_results=5)
        search_tool = DuckDuckGoSearchRun(api_wrapper=search_wrapper)
        
        news_query = f"{query} site:reuters.com OR site:bbc.com OR site:cnn.com OR site:npr.org OR site:apnews.com"
        results = search_tool.run(news_query)
        
        return f"Recent news about '{query}':\n{results}"
        
    except Exception as e:
        return f"Error searching news: {str(e)}"

def enhanced_web_search(query: str) -> str:
    """
    Enhanced web search that combines multiple search strategies.
    """
    try:
        search_wrapper = DuckDuckGoSearchAPIWrapper(max_results=8)
        search_tool = DuckDuckGoSearchRun(api_wrapper=search_wrapper)
        
        # Perform search
        results = search_tool.run(query)
        
        # Add timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        return f"Web search results for '{query}' (searched at {timestamp}):\n{results}"
        
    except Exception as e:
        return f"Error performing web search: {str(e)}"

def get_research_tools():
    """Return a comprehensive list of tools for the research agent"""
    
    # Wikipedia tool
    wikipedia = WikipediaQueryRun(
        api_wrapper=WikipediaAPIWrapper(
            top_k_results=3,
            doc_content_chars_max=3000
        )
    )
    
    # Web search tool
    web_search = Tool(
        name="web_search",
        description="Search the web for current information, news, and general knowledge. Use this for recent developments, current events, or when Wikipedia doesn't have enough information.",
        func=enhanced_web_search
    )
    
    # News search tool
    news_search = Tool(
        name="news_search",
        description="Search for recent news articles and current events related to the query. Use this specifically for latest news and recent developments.",
        func=search_news
    )
    
    # Academic papers search
    arxiv_search = ArxivQueryRun(
        api_wrapper=ArxivAPIWrapper(
            top_k_results=3,
            doc_content_chars_max=2000
        )
    )
    
    # Web content extraction tool
    web_content_tool = Tool(
        name="get_web_content",
        description="Extract text content from a specific web page URL. Use this when you have a specific URL and want to get detailed content from it.",
        func=get_web_content
    )
    
    return [wikipedia, web_search, news_search, arxiv_search, web_content_tool]
