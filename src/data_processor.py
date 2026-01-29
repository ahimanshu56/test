"""
Data Processing Module
Handles data transformations, calculations, and processing operations.
"""

from typing import List, Dict, Any, Optional
import statistics


class DataProcessor:
    """Process and transform data."""
    
    def __init__(self):
        self.cache: Dict[str, Any] = {}
    
    def normalize_data(self, data: List[float], min_val: float = 0.0, max_val: float = 1.0) -> List[float]:
        """
        Normalize data to a specified range.
        
        Args:
            data: List of numeric values
            min_val: Minimum value of output range
            max_val: Maximum value of output range
            
        Returns:
            Normalized data
            
        Raises:
            ValueError: If data is empty or invalid
        """
        if not data:
            raise ValueError("Data cannot be empty")
        
        if min_val >= max_val:
            raise ValueError("min_val must be less than max_val")
        
        data_min = min(data)
        data_max = max(data)
        
        if data_min == data_max:
            # All values are the same
            return [min_val] * len(data)
        
        normalized = []
        for value in data:
            norm_value = (value - data_min) / (data_max - data_min)
            scaled_value = norm_value * (max_val - min_val) + min_val
            normalized.append(scaled_value)
        
        return normalized
    
    def calculate_statistics(self, data: List[float]) -> Dict[str, float]:
        """
        Calculate statistical measures for data.
        
        Args:
            data: List of numeric values
            
        Returns:
            Dictionary with statistical measures
            
        Raises:
            ValueError: If data is empty or invalid
        """
        if not data:
            raise ValueError("Data cannot be empty")
        
        if len(data) == 1:
            return {
                'mean': data[0],
                'median': data[0],
                'std_dev': 0.0,
                'min': data[0],
                'max': data[0],
                'count': 1
            }
        
        return {
            'mean': statistics.mean(data),
            'median': statistics.median(data),
            'std_dev': statistics.stdev(data),
            'min': min(data),
            'max': max(data),
            'count': len(data)
        }
    
    def filter_outliers(self, data: List[float], std_threshold: float = 2.0) -> List[float]:
        """
        Remove outliers from data using standard deviation method.
        
        Args:
            data: List of numeric values
            std_threshold: Number of standard deviations for outlier detection
            
        Returns:
            Filtered data without outliers
        """
        if not data or len(data) < 3:
            return data.copy()
        
        mean = statistics.mean(data)
        std_dev = statistics.stdev(data)
        
        if std_dev == 0:
            return data.copy()
        
        filtered = []
        for value in data:
            z_score = abs((value - mean) / std_dev)
            if z_score <= std_threshold:
                filtered.append(value)
        
        return filtered
    
    def aggregate_by_key(self, data: List[Dict], key: str, value_key: str, operation: str = 'sum') -> Dict[Any, float]:
        """
        Aggregate data by a specific key.
        
        Args:
            data: List of dictionaries
            key: Key to group by
            value_key: Key containing values to aggregate
            operation: Aggregation operation ('sum', 'avg', 'min', 'max', 'count')
            
        Returns:
            Dictionary with aggregated results
            
        Raises:
            ValueError: If operation is invalid
        """
        if not data:
            return {}
        
        valid_operations = ['sum', 'avg', 'min', 'max', 'count']
        if operation not in valid_operations:
            raise ValueError(f"Invalid operation. Must be one of {valid_operations}")
        
        groups: Dict[Any, List[float]] = {}
        
        for item in data:
            if key not in item:
                continue
            
            group_key = item[key]
            
            if operation == 'count':
                if group_key not in groups:
                    groups[group_key] = []
                groups[group_key].append(1)
            else:
                if value_key not in item:
                    continue
                
                if group_key not in groups:
                    groups[group_key] = []
                
                try:
                    groups[group_key].append(float(item[value_key]))
                except (ValueError, TypeError):
                    continue
        
        result = {}
        for group_key, values in groups.items():
            if not values:
                continue
            
            if operation == 'sum' or operation == 'count':
                result[group_key] = sum(values)
            elif operation == 'avg':
                result[group_key] = sum(values) / len(values)
            elif operation == 'min':
                result[group_key] = min(values)
            elif operation == 'max':
                result[group_key] = max(values)
        
        return result
    
    def transform_data(self, data: List[Dict], transformations: Dict[str, str]) -> List[Dict]:
        """
        Apply transformations to data fields.
        
        Args:
            data: List of dictionaries
            transformations: Dict mapping field names to transformation types
                           ('upper', 'lower', 'strip', 'int', 'float')
            
        Returns:
            Transformed data
        """
        if not data:
            return []
        
        transformed = []
        for item in data.copy():
            new_item = item.copy()
            
            for field, transform_type in transformations.items():
                if field not in new_item:
                    continue
                
                value = new_item[field]
                
                try:
                    if transform_type == 'upper' and isinstance(value, str):
                        new_item[field] = value.upper()
                    elif transform_type == 'lower' and isinstance(value, str):
                        new_item[field] = value.lower()
                    elif transform_type == 'strip' and isinstance(value, str):
                        new_item[field] = value.strip()
                    elif transform_type == 'int':
                        new_item[field] = int(value)
                    elif transform_type == 'float':
                        new_item[field] = float(value)
                except (ValueError, TypeError, AttributeError):
                    # Keep original value if transformation fails
                    pass
            
            transformed.append(new_item)
        
        return transformed
    
    def cache_result(self, key: str, value: Any) -> None:
        """Cache a result for later retrieval."""
        self.cache[key] = value
    
    def get_cached_result(self, key: str) -> Optional[Any]:
        """Retrieve a cached result."""
        return self.cache.get(key)
    
    def clear_cache(self) -> None:
        """Clear all cached results."""
        self.cache.clear()
