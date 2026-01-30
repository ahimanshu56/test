"""
Data processing module for calculations and transformations.
"""
from typing import List, Dict, Any, Optional
import statistics


class DataProcessor:
    """Process and analyze data."""
    
    def calculate_statistics(self, numbers: List[float]) -> Dict[str, float]:
        """Calculate statistical measures for a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate statistics for empty list")
        
        if not all(isinstance(n, (int, float)) for n in numbers):
            raise TypeError("All elements must be numbers")
        
        result = {
            "mean": statistics.mean(numbers),
            "median": statistics.median(numbers),
            "min": min(numbers),
            "max": max(numbers),
            "count": len(numbers)
        }
        
        if len(numbers) > 1:
            result["stdev"] = statistics.stdev(numbers)
        else:
            result["stdev"] = 0.0
        
        return result
    
    def filter_outliers(self, numbers: List[float], threshold: float = 2.0) -> List[float]:
        """Remove outliers using standard deviation method."""
        if not numbers:
            return []
        
        if len(numbers) < 3:
            return numbers.copy()
        
        mean = statistics.mean(numbers)
        stdev = statistics.stdev(numbers)
        
        if stdev == 0:
            return numbers.copy()
        
        filtered = [
            n for n in numbers
            if abs(n - mean) <= threshold * stdev
        ]
        
        return filtered
    
    def normalize_data(self, numbers: List[float], min_val: float = 0.0, max_val: float = 1.0) -> List[float]:
        """Normalize numbers to a specified range."""
        if not numbers:
            return []
        
        if min_val >= max_val:
            raise ValueError("min_val must be less than max_val")
        
        data_min = min(numbers)
        data_max = max(numbers)
        
        if data_min == data_max:
            # All values are the same
            return [(min_val + max_val) / 2] * len(numbers)
        
        normalized = []
        for n in numbers:
            normalized_value = (n - data_min) / (data_max - data_min)
            scaled_value = normalized_value * (max_val - min_val) + min_val
            normalized.append(scaled_value)
        
        return normalized
    
    def group_by_range(self, numbers: List[float], range_size: float) -> Dict[str, List[float]]:
        """Group numbers into ranges."""
        if not numbers:
            return {}
        
        if range_size <= 0:
            raise ValueError("range_size must be positive")
        
        groups = {}
        
        for n in numbers:
            range_start = (n // range_size) * range_size
            range_end = range_start + range_size
            key = f"{range_start}-{range_end}"
            
            if key not in groups:
                groups[key] = []
            
            groups[key].append(n)
        
        return groups
    
    def transform_data(self, data: List[Dict[str, Any]], key: str, operation: str) -> List[Any]:
        """Transform data by applying operation to specified key."""
        if not data:
            return []
        
        if operation not in ["sum", "count", "avg", "max", "min", "list"]:
            raise ValueError(f"Unsupported operation: {operation}")
        
        values = []
        for item in data:
            if not isinstance(item, dict):
                continue
            
            if key in item:
                values.append(item[key])
        
        if not values:
            return []
        
        if operation == "sum":
            return [sum(v for v in values if isinstance(v, (int, float)))]
        elif operation == "count":
            return [len(values)]
        elif operation == "avg":
            numeric_values = [v for v in values if isinstance(v, (int, float))]
            if not numeric_values:
                return []
            return [sum(numeric_values) / len(numeric_values)]
        elif operation == "max":
            return [max(values)]
        elif operation == "min":
            return [min(values)]
        elif operation == "list":
            return values
        
        return []
    
    def merge_datasets(self, dataset1: List[Dict], dataset2: List[Dict], key: str) -> List[Dict]:
        """Merge two datasets on a common key."""
        if not dataset1 and not dataset2:
            return []
        
        if not dataset1:
            return dataset2.copy()
        
        if not dataset2:
            return dataset1.copy()
        
        # Create lookup for dataset2
        lookup = {item.get(key): item for item in dataset2 if key in item}
        
        merged = []
        for item1 in dataset1:
            if key not in item1:
                merged.append(item1.copy())
                continue
            
            key_value = item1[key]
            if key_value in lookup:
                # Merge the two items
                merged_item = {**item1, **lookup[key_value]}
                merged.append(merged_item)
            else:
                merged.append(item1.copy())
        
        return merged
