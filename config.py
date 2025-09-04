"""
Configuration management for the Research Agent
"""
import os
import json
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class AgentConfig:
    """Configuration settings for the research agent"""
    
    # Model settings
    model_name: str = "claude-3-5-sonnet-20240620"
    temperature: float = 0.1
    max_tokens: Optional[int] = None
    
    # Search settings
    max_search_results: int = 8
    max_wikipedia_results: int = 3
    max_arxiv_results: int = 3
    max_news_results: int = 5
    
    # Output settings
    max_key_points: int = 10
    summary_max_length: int = 500
    
    # File settings
    output_directory: str = "research_outputs"
    auto_save: bool = False
    default_format: str = "json"  # json, txt, pdf, all
    
    # UI settings
    use_rich_formatting: bool = True
    show_progress_bars: bool = True
    verbose_mode: bool = False
    
    # Cache settings
    enable_caching: bool = True
    cache_duration_hours: int = 24
    cache_directory: str = ".cache"

class ConfigManager:
    """Manages configuration loading and saving"""
    
    def __init__(self, config_file: str = "agent_config.json"):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self) -> AgentConfig:
        """Load configuration from file or create default"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                return AgentConfig(**data)
            except (json.JSONDecodeError, TypeError) as e:
                print(f"Warning: Error loading config file: {e}")
                print("Using default configuration...")
        
        # Create default config
        config = AgentConfig()
        self.save_config(config)
        return config
    
    def save_config(self, config: AgentConfig) -> None:
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(asdict(config), f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save config: {e}")
    
    def update_config(self, **kwargs) -> None:
        """Update specific configuration values"""
        for key, value in kwargs.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)
        self.save_config(self.config)
    
    def get_config(self) -> AgentConfig:
        """Get current configuration"""
        return self.config
    
    def reset_to_defaults(self) -> None:
        """Reset configuration to defaults"""
        self.config = AgentConfig()
        self.save_config(self.config)

# Global config manager instance
config_manager = ConfigManager()

def get_config() -> AgentConfig:
    """Get the current configuration"""
    return config_manager.get_config()

def update_config(**kwargs) -> None:
    """Update configuration settings"""
    config_manager.update_config(**kwargs)

def ensure_directories() -> None:
    """Ensure required directories exist"""
    config = get_config()
    
    # Create output directory
    Path(config.output_directory).mkdir(exist_ok=True)
    
    # Create cache directory if caching is enabled
    if config.enable_caching:
        Path(config.cache_directory).mkdir(exist_ok=True)
