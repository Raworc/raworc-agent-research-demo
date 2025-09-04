"""
Caching system for the Research Agent
"""
import os
import json
import hashlib
import time
from typing import Optional, Any, Dict
from pathlib import Path
from config import get_config

class CacheManager:
    """Manages caching of research results and API responses"""
    
    def __init__(self):
        self.config = get_config()
        self.cache_dir = Path(self.config.cache_directory)
        self.cache_dir.mkdir(exist_ok=True)
    
    def _get_cache_key(self, query: str, tool_name: str = "general") -> str:
        """Generate a cache key for a query"""
        combined = f"{tool_name}:{query.lower().strip()}"
        return hashlib.md5(combined.encode()).hexdigest()
    
    def _get_cache_file(self, cache_key: str) -> Path:
        """Get the cache file path for a given key"""
        return self.cache_dir / f"{cache_key}.json"
    
    def _is_cache_valid(self, cache_file: Path) -> bool:
        """Check if cache file is still valid (not expired)"""
        if not cache_file.exists():
            return False
        
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            cached_time = data.get('timestamp', 0)
            current_time = time.time()
            
            # Check if cache is within the valid duration
            cache_duration_seconds = self.config.cache_duration_hours * 3600
            return (current_time - cached_time) < cache_duration_seconds
            
        except (json.JSONDecodeError, KeyError):
            return False
    
    def get_cached_result(self, query: str, tool_name: str = "general") -> Optional[Any]:
        """Get cached result for a query"""
        if not self.config.enable_caching:
            return None
        
        cache_key = self._get_cache_key(query, tool_name)
        cache_file = self._get_cache_file(cache_key)
        
        if self._is_cache_valid(cache_file):
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data.get('result')
            except (json.JSONDecodeError, KeyError):
                pass
        
        return None
    
    def cache_result(self, query: str, result: Any, tool_name: str = "general") -> None:
        """Cache a result for a query"""
        if not self.config.enable_caching:
            return
        
        cache_key = self._get_cache_key(query, tool_name)
        cache_file = self._get_cache_file(cache_key)
        
        cache_data = {
            'query': query,
            'tool_name': tool_name,
            'result': result,
            'timestamp': time.time()
        }
        
        try:
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not cache result: {e}")
    
    def clear_cache(self) -> int:
        """Clear all cached files and return count of files deleted"""
        deleted_count = 0
        
        if self.cache_dir.exists():
            for cache_file in self.cache_dir.glob("*.json"):
                try:
                    cache_file.unlink()
                    deleted_count += 1
                except Exception as e:
                    print(f"Warning: Could not delete cache file {cache_file}: {e}")
        
        return deleted_count
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Get statistics about the cache"""
        if not self.cache_dir.exists():
            return {'total_files': 0, 'total_size_mb': 0, 'valid_files': 0}
        
        total_files = 0
        total_size = 0
        valid_files = 0
        
        for cache_file in self.cache_dir.glob("*.json"):
            total_files += 1
            total_size += cache_file.stat().st_size
            
            if self._is_cache_valid(cache_file):
                valid_files += 1
        
        return {
            'total_files': total_files,
            'total_size_mb': round(total_size / (1024 * 1024), 2),
            'valid_files': valid_files,
            'expired_files': total_files - valid_files
        }
    
    def cleanup_expired_cache(self) -> int:
        """Remove expired cache files and return count of files deleted"""
        deleted_count = 0
        
        if not self.cache_dir.exists():
            return 0
        
        for cache_file in self.cache_dir.glob("*.json"):
            if not self._is_cache_valid(cache_file):
                try:
                    cache_file.unlink()
                    deleted_count += 1
                except Exception as e:
                    print(f"Warning: Could not delete expired cache file {cache_file}: {e}")
        
        return deleted_count

# Global cache manager instance
cache_manager = CacheManager()

def get_cached_result(query: str, tool_name: str = "general") -> Optional[Any]:
    """Get cached result for a query"""
    return cache_manager.get_cached_result(query, tool_name)

def cache_result(query: str, result: Any, tool_name: str = "general") -> None:
    """Cache a result for a query"""
    cache_manager.cache_result(query, result, tool_name)

def clear_cache() -> int:
    """Clear all cached files"""
    return cache_manager.clear_cache()

def get_cache_stats() -> Dict[str, Any]:
    """Get cache statistics"""
    return cache_manager.get_cache_stats()

def cleanup_expired_cache() -> int:
    """Remove expired cache files"""
    return cache_manager.cleanup_expired_cache()
