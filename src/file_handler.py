"""File handling utilities."""
import os
import json
from typing import Any, Dict, List, Optional


class FileHandler:
    """Handle file operations."""
    
    @staticmethod
    def read_file(filepath: str) -> str:
        """Read content from a file."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    @staticmethod
    def write_file(filepath: str, content: str) -> bool:
        """Write content to a file."""
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception:
            return False
    
    @staticmethod
    def append_to_file(filepath: str, content: str) -> bool:
        """Append content to a file."""
        try:
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception:
            return False
    
    @staticmethod
    def read_json(filepath: str) -> Dict[str, Any]:
        """Read JSON from a file."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    @staticmethod
    def write_json(filepath: str, data: Dict[str, Any]) -> bool:
        """Write data to JSON file."""
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception:
            return False
    
    @staticmethod
    def file_exists(filepath: str) -> bool:
        """Check if file exists."""
        return os.path.exists(filepath) and os.path.isfile(filepath)
    
    @staticmethod
    def get_file_size(filepath: str) -> int:
        """Get file size in bytes."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        return os.path.getsize(filepath)
    
    @staticmethod
    def list_files(directory: str, extension: Optional[str] = None) -> List[str]:
        """List files in directory, optionally filtered by extension."""
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")
        
        files = []
        for item in os.listdir(directory):
            filepath = os.path.join(directory, item)
            if os.path.isfile(filepath):
                if extension is None or item.endswith(extension):
                    files.append(item)
        return sorted(files)
    
    @staticmethod
    def delete_file(filepath: str) -> bool:
        """Delete a file."""
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
            return False
        except Exception:
            return False
