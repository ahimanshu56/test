"""Data processing utilities."""
from typing import List, Dict, Any, Union
import statistics


class DataProcessor:
    """Process and analyze data."""
    
    @staticmethod
    def filter_positive(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
        """Filter out negative numbers and zero."""
        return [n for n in numbers if n > 0]
    
    @staticmethod
    def filter_negative(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
        """Filter out positive numbers and zero."""
        return [n for n in numbers if n < 0]
    
    @staticmethod
    def calculate_mean(numbers: List[Union[int, float]]) -> float:
        """Calculate mean of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate mean of empty list")
        return statistics.mean(numbers)
    
    @staticmethod
    def calculate_median(numbers: List[Union[int, float]]) -> float:
        """Calculate median of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate median of empty list")
        return statistics.median(numbers)
    
    @staticmethod
    def calculate_std_dev(numbers: List[Union[int, float]]) -> float:
        """Calculate standard deviation."""
        if len(numbers) < 2:
            raise ValueError("Need at least 2 numbers for standard deviation")
        return statistics.stdev(numbers)
    
    @staticmethod
    def find_outliers(numbers: List[Union[int, float]], threshold: float = 2.0) -> List[Union[int, float]]:
        """Find outliers using standard deviation method."""
        if len(numbers) < 3:
            return []
        
        mean = statistics.mean(numbers)
        std_dev = statistics.stdev(numbers)
        
        outliers = []
        for num in numbers:
            z_score = abs((num - mean) / std_dev) if std_dev > 0 else 0
            if z_score > threshold:
                outliers.append(num)
        
        return outliers
    
    @staticmethod
    def normalize(numbers: List[Union[int, float]]) -> List[float]:
        """Normalize numbers to 0-1 range."""
        if not numbers:
            return []
        
        min_val = min(numbers)
        max_val = max(numbers)
        
        if min_val == max_val:
            return [0.5] * len(numbers)
        
        return [(n - min_val) / (max_val - min_val) for n in numbers]
    
    @staticmethod
    def group_by_range(numbers: List[Union[int, float]], range_size: int) -> Dict[str, List[Union[int, float]]]:
        """Group numbers by ranges."""
        if range_size <= 0:
            raise ValueError("Range size must be positive")
        
        groups = {}
        for num in numbers:
            range_start = (int(num) // range_size) * range_size
            range_key = f"{range_start}-{range_start + range_size - 1}"
            
            if range_key not in groups:
                groups[range_key] = []
            groups[range_key].append(num)
        
        return groups
    
    @staticmethod
    def remove_duplicates(items: List[Any]) -> List[Any]:
        """Remove duplicates while preserving order."""
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
