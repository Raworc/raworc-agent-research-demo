"""
Research templates for different domains and use cases
"""
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class ResearchTemplate:
    """A research template with predefined queries and instructions"""
    name: str
    description: str
    queries: List[str]
    focus_areas: List[str]
    suggested_tools: List[str]

class TemplateManager:
    """Manages research templates"""
    
    def __init__(self):
        self.templates = self._initialize_templates()
    
    def _initialize_templates(self) -> Dict[str, ResearchTemplate]:
        """Initialize predefined research templates"""
        templates = {}
        
        # Technology Research Template
        templates["technology"] = ResearchTemplate(
            name="Technology Research",
            description="Comprehensive research on technology topics, trends, and innovations",
            queries=[
                "What is {topic} and how does it work?",
                "What are the latest developments in {topic}?",
                "What are the advantages and disadvantages of {topic}?",
                "What are the current applications of {topic} in industry?",
                "What is the future outlook for {topic}?"
            ],
            focus_areas=[
                "Technical definition and explanation",
                "Current market trends and adoption",
                "Benefits and limitations",
                "Real-world applications",
                "Future predictions and developments"
            ],
            suggested_tools=["wikipedia", "web_search", "news_search", "arxiv"]
        )
        
        # Business Analysis Template
        templates["business"] = ResearchTemplate(
            name="Business Analysis",
            description="Research framework for business topics, companies, and market analysis",
            queries=[
                "What is the current state of {topic} in the market?",
                "Who are the key players in {topic}?",
                "What are the recent trends and developments in {topic}?",
                "What challenges and opportunities exist in {topic}?",
                "What is the financial outlook for {topic}?"
            ],
            focus_areas=[
                "Market overview and size",
                "Key competitors and market leaders",
                "Recent trends and news",
                "Challenges and opportunities",
                "Financial performance and outlook"
            ],
            suggested_tools=["web_search", "news_search", "wikipedia"]
        )
        
        # Academic Research Template
        templates["academic"] = ResearchTemplate(
            name="Academic Research",
            description="Scholarly research approach for academic topics and literature review",
            queries=[
                "What does current research say about {topic}?",
                "What are the key theories and concepts related to {topic}?",
                "What are recent academic findings about {topic}?",
                "What methodologies are used to study {topic}?",
                "What are the current debates and controversies around {topic}?"
            ],
            focus_areas=[
                "Literature review and key studies",
                "Theoretical frameworks",
                "Recent research findings",
                "Research methodologies",
                "Academic debates and discussions"
            ],
            suggested_tools=["arxiv", "wikipedia", "web_search"]
        )
        
        # Health & Medicine Template
        templates["health"] = ResearchTemplate(
            name="Health & Medicine",
            description="Research framework for health, medical, and wellness topics",
            queries=[
                "What is {topic} and what causes it?",
                "What are the symptoms and diagnosis methods for {topic}?",
                "What are the current treatment options for {topic}?",
                "What does recent medical research say about {topic}?",
                "What are the prevention strategies for {topic}?"
            ],
            focus_areas=[
                "Medical definition and causes",
                "Symptoms and diagnostic criteria",
                "Treatment options and effectiveness",
                "Latest medical research",
                "Prevention and risk factors"
            ],
            suggested_tools=["wikipedia", "arxiv", "web_search", "news_search"]
        )
        
        # Historical Research Template
        templates["historical"] = ResearchTemplate(
            name="Historical Research",
            description="Research framework for historical events, periods, and figures",
            queries=[
                "What happened during {topic} and when?",
                "What were the causes and context of {topic}?",
                "Who were the key figures involved in {topic}?",
                "What were the consequences and impact of {topic}?",
                "How is {topic} viewed by modern historians?"
            ],
            focus_areas=[
                "Timeline and key events",
                "Historical context and causes",
                "Important figures and their roles",
                "Immediate and long-term consequences",
                "Modern historical interpretation"
            ],
            suggested_tools=["wikipedia", "web_search"]
        )
        
        # Comparative Analysis Template
        templates["comparative"] = ResearchTemplate(
            name="Comparative Analysis",
            description="Framework for comparing two or more topics, concepts, or entities",
            queries=[
                "What are the key differences between {topic}?",
                "What are the similarities between {topic}?",
                "What are the advantages and disadvantages of each in {topic}?",
                "In what situations is each better suited in {topic}?",
                "What do experts recommend regarding {topic}?"
            ],
            focus_areas=[
                "Key differences and distinctions",
                "Common features and similarities",
                "Pros and cons of each option",
                "Use cases and applications",
                "Expert opinions and recommendations"
            ],
            suggested_tools=["wikipedia", "web_search", "news_search"]
        )
        
        return templates
    
    def get_template(self, template_name: str) -> ResearchTemplate:
        """Get a specific template by name"""
        return self.templates.get(template_name.lower())
    
    def list_templates(self) -> List[Tuple[str, str]]:
        """Get list of available templates with their descriptions"""
        return [(name, template.description) for name, template in self.templates.items()]
    
    def generate_queries(self, template_name: str, topic: str) -> List[str]:
        """Generate queries for a specific topic using a template"""
        template = self.get_template(template_name)
        if not template:
            return []
        
        return [query.format(topic=topic) for query in template.queries]
    
    def get_template_info(self, template_name: str) -> Dict:
        """Get detailed information about a template"""
        template = self.get_template(template_name)
        if not template:
            return {}
        
        return {
            "name": template.name,
            "description": template.description,
            "focus_areas": template.focus_areas,
            "suggested_tools": template.suggested_tools,
            "sample_queries": template.queries[:3]  # Show first 3 queries as samples
        }

# Global template manager instance
template_manager = TemplateManager()

def get_available_templates() -> List[Tuple[str, str]]:
    """Get list of available research templates"""
    return template_manager.list_templates()

def get_template_queries(template_name: str, topic: str) -> List[str]:
    """Generate research queries using a template"""
    return template_manager.generate_queries(template_name, topic)

def get_template_info(template_name: str) -> Dict:
    """Get information about a specific template"""
    return template_manager.get_template_info(template_name)
