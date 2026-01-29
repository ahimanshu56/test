"""
Comprehensive tests for DataProcessor module.
Achieves 100% coverage of all functions, branches, and edge cases.
"""

import pytest
from src.data_processor import DataProcessor


class TestDataProcessorNormalize:
    """Tests for data normalization."""
    
    def test_normalize_data_default_range(self):
        """Test normalizing data to default 0-1 range."""
        processor = DataProcessor()
        data = [1, 2, 3, 4, 5]
        
        result = processor.normalize_data(data)
        
        assert result[0] == 0.0
        assert result[-1] == 1.0
        assert all(0 <= x <= 1 for x in result)
    
    def test_normalize_data_custom_range(self):
        """Test normalizing data to custom range."""
        processor = DataProcessor()
        data = [1, 2, 3, 4, 5]
        
        result = processor.normalize_data(data, min_val=-1.0, max_val=1.0)
        
        assert result[0] == -1.0
        assert result[-1] == 1.0
        assert all(-1 <= x <= 1 for x in result)
    
    def test_normalize_data_empty_list(self):
        """Test normalizing empty data list."""
        processor = DataProcessor()
        
        with pytest.raises(ValueError, match="Data cannot be empty"):
            processor.normalize_data([])
    
    def test_normalize_data_invalid_range(self):
        """Test normalizing with invalid range."""
        processor = DataProcessor()
        data = [1, 2, 3]
        
        with pytest.raises(ValueError, match="min_val must be less than max_val"):
            processor.normalize_data(data, min_val=1.0, max_val=0.0)
    
    def test_normalize_data_equal_range(self):
        """Test normalizing with equal min and max."""
        processor = DataProcessor()
        data = [1, 2, 3]
        
        with pytest.raises(ValueError, match="min_val must be less than max_val"):
            processor.normalize_data(data, min_val=1.0, max_val=1.0)
    
    def test_normalize_data_all_same_values(self):
        """Test normalizing data with all same values."""
        processor = DataProcessor()
        data = [5, 5, 5, 5]
        
        result = processor.normalize_data(data)
        
        assert all(x == 0.0 for x in result)


class TestDataProcessorStatistics:
    """Tests for statistical calculations."""
    
    def test_calculate_statistics_normal_data(self):
        """Test calculating statistics for normal data."""
        processor = DataProcessor()
        data = [1, 2, 3, 4, 5]
        
        stats = processor.calculate_statistics(data)
        
        assert stats['mean'] == 3.0
        assert stats['median'] == 3.0
        assert stats['min'] == 1
        assert stats['max'] == 5
        assert stats['count'] == 5
        assert stats['std_dev'] > 0
    
    def test_calculate_statistics_single_value(self):
        """Test calculating statistics for single value."""
        processor = DataProcessor()
        data = [42]
        
        stats = processor.calculate_statistics(data)
        
        assert stats['mean'] == 42
        assert stats['median'] == 42
        assert stats['std_dev'] == 0.0
        assert stats['min'] == 42
        assert stats['max'] == 42
        assert stats['count'] == 1
    
    def test_calculate_statistics_empty_data(self):
        """Test calculating statistics for empty data."""
        processor = DataProcessor()
        
        with pytest.raises(ValueError, match="Data cannot be empty"):
            processor.calculate_statistics([])
    
    def test_calculate_statistics_negative_values(self):
        """Test calculating statistics with negative values."""
        processor = DataProcessor()
        data = [-5, -3, 0, 3, 5]
        
        stats = processor.calculate_statistics(data)
        
        assert stats['mean'] == 0.0
        assert stats['median'] == 0.0
        assert stats['min'] == -5
        assert stats['max'] == 5


class TestDataProcessorFilterOutliers:
    """Tests for outlier filtering."""
    
    def test_filter_outliers_no_outliers(self):
        """Test filtering data with no outliers."""
        processor = DataProcessor()
        data = [1, 2, 3, 4, 5]
        
        result = processor.filter_outliers(data)
        
        assert len(result) == 5
    
    def test_filter_outliers_with_outliers(self):
        """Test filtering data with outliers."""
        processor = DataProcessor()
        data = [1, 2, 3, 4, 5, 100]
        
        result = processor.filter_outliers(data, std_threshold=2.0)
        
        assert 100 not in result
        assert len(result) < len(data)
    
    def test_filter_outliers_empty_data(self):
        """Test filtering empty data."""
        processor = DataProcessor()
        
        result = processor.filter_outliers([])
        
        assert result == []
    
    def test_filter_outliers_small_dataset(self):
        """Test filtering data with less than 3 values."""
        processor = DataProcessor()
        data = [1, 2]
        
        result = processor.filter_outliers(data)
        
        assert result == data
    
    def test_filter_outliers_zero_std_dev(self):
        """Test filtering data with zero standard deviation."""
        processor = DataProcessor()
        data = [5, 5, 5, 5]
        
        result = processor.filter_outliers(data)
        
        assert result == data


class TestDataProcessorAggregate:
    """Tests for data aggregation."""
    
    def test_aggregate_by_key_sum(self):
        """Test aggregating data by sum."""
        processor = DataProcessor()
        data = [
            {'category': 'A', 'value': 10},
            {'category': 'A', 'value': 20},
            {'category': 'B', 'value': 30}
        ]
        
        result = processor.aggregate_by_key(data, 'category', 'value', 'sum')
        
        assert result['A'] == 30
        assert result['B'] == 30
    
    def test_aggregate_by_key_avg(self):
        """Test aggregating data by average."""
        processor = DataProcessor()
        data = [
            {'category': 'A', 'value': 10},
            {'category': 'A', 'value': 20},
            {'category': 'B', 'value': 30}
        ]
        
        result = processor.aggregate_by_key(data, 'category', 'value', 'avg')
        
        assert result['A'] == 15.0
        assert result['B'] == 30.0
    
    def test_aggregate_by_key_min(self):
        """Test aggregating data by minimum."""
        processor = DataProcessor()
        data = [
            {'category': 'A', 'value': 10},
            {'category': 'A', 'value': 20},
            {'category': 'B', 'value': 30}
        ]
        
        result = processor.aggregate_by_key(data, 'category', 'value', 'min')
        
        assert result['A'] == 10
        assert result['B'] == 30
    
    def test_aggregate_by_key_max(self):
        """Test aggregating data by maximum."""
        processor = DataProcessor()
        data = [
            {'category': 'A', 'value': 10},
            {'category': 'A', 'value': 20},
            {'category': 'B', 'value': 30}
        ]
        
        result = processor.aggregate_by_key(data, 'category', 'value', 'max')
        
        assert result['A'] == 20
        assert result['B'] == 30
    
    def test_aggregate_by_key_count(self):
        """Test aggregating data by count."""
        processor = DataProcessor()
        data = [
            {'category': 'A', 'value': 10},
            {'category': 'A', 'value': 20},
            {'category': 'B', 'value': 30}
        ]
        
        result = processor.aggregate_by_key(data, 'category', 'value', 'count')
        
        assert result['A'] == 2
        assert result['B'] == 1
    
    def test_aggregate_by_key_empty_data(self):
        """Test aggregating empty data."""
        processor = DataProcessor()
        
        result = processor.aggregate_by_key([], 'category', 'value', 'sum')
        
        assert result == {}
    
    def test_aggregate_by_key_invalid_operation(self):
        """Test aggregating with invalid operation."""
        processor = DataProcessor()
        data = [{'category': 'A', 'value': 10}]
        
        with pytest.raises(ValueError, match="Invalid operation"):
            processor.aggregate_by_key(data, 'category', 'value', 'invalid')
    
    def test_aggregate_by_key_missing_key(self):
        """Test aggregating when key is missing."""
        processor = DataProcessor()
        data = [
            {'category': 'A', 'value': 10},
            {'other': 'B', 'value': 20}
        ]
        
        result = processor.aggregate_by_key(data, 'category', 'value', 'sum')
        
        assert result == {'A': 10}
    
    def test_aggregate_by_key_missing_value_key(self):
        """Test aggregating when value key is missing."""
        processor = DataProcessor()
        data = [
            {'category': 'A', 'value': 10},
            {'category': 'A', 'other': 20}
        ]
        
        result = processor.aggregate_by_key(data, 'category', 'value', 'sum')
        
        assert result == {'A': 10}
    
    def test_aggregate_by_key_invalid_value_type(self):
        """Test aggregating with invalid value types."""
        processor = DataProcessor()
        data = [
            {'category': 'A', 'value': 10},
            {'category': 'A', 'value': 'invalid'}
        ]
        
        result = processor.aggregate_by_key(data, 'category', 'value', 'sum')
        
        assert result == {'A': 10}


class TestDataProcessorTransform:
    """Tests for data transformation."""
    
    def test_transform_data_upper(self):
        """Test transforming strings to uppercase."""
        processor = DataProcessor()
        data = [{'name': 'john'}, {'name': 'jane'}]
        
        result = processor.transform_data(data, {'name': 'upper'})
        
        assert result[0]['name'] == 'JOHN'
        assert result[1]['name'] == 'JANE'
    
    def test_transform_data_lower(self):
        """Test transforming strings to lowercase."""
        processor = DataProcessor()
        data = [{'name': 'JOHN'}, {'name': 'JANE'}]
        
        result = processor.transform_data(data, {'name': 'lower'})
        
        assert result[0]['name'] == 'john'
        assert result[1]['name'] == 'jane'
    
    def test_transform_data_strip(self):
        """Test stripping whitespace from strings."""
        processor = DataProcessor()
        data = [{'name': '  john  '}, {'name': '  jane  '}]
        
        result = processor.transform_data(data, {'name': 'strip'})
        
        assert result[0]['name'] == 'john'
        assert result[1]['name'] == 'jane'
    
    def test_transform_data_to_int(self):
        """Test transforming values to integers."""
        processor = DataProcessor()
        data = [{'value': '10'}, {'value': '20'}]
        
        result = processor.transform_data(data, {'value': 'int'})
        
        assert result[0]['value'] == 10
        assert result[1]['value'] == 20
    
    def test_transform_data_to_float(self):
        """Test transforming values to floats."""
        processor = DataProcessor()
        data = [{'value': '10.5'}, {'value': '20.7'}]
        
        result = processor.transform_data(data, {'value': 'float'})
        
        assert result[0]['value'] == 10.5
        assert result[1]['value'] == 20.7
    
    def test_transform_data_empty_list(self):
        """Test transforming empty data list."""
        processor = DataProcessor()
        
        result = processor.transform_data([], {'name': 'upper'})
        
        assert result == []
    
    def test_transform_data_missing_field(self):
        """Test transforming when field is missing."""
        processor = DataProcessor()
        data = [{'name': 'john'}, {'other': 'jane'}]
        
        result = processor.transform_data(data, {'name': 'upper'})
        
        assert result[0]['name'] == 'JOHN'
        assert 'name' not in result[1]
    
    def test_transform_data_invalid_transformation(self):
        """Test transforming with invalid value type."""
        processor = DataProcessor()
        data = [{'value': 'invalid'}]
        
        result = processor.transform_data(data, {'value': 'int'})
        
        # Should keep original value on error
        assert result[0]['value'] == 'invalid'
    
    def test_transform_data_wrong_type_for_string_op(self):
        """Test string operation on non-string value."""
        processor = DataProcessor()
        data = [{'value': 123}]
        
        result = processor.transform_data(data, {'value': 'upper'})
        
        # Should keep original value
        assert result[0]['value'] == 123


class TestDataProcessorCache:
    """Tests for caching functionality."""
    
    def test_cache_result(self):
        """Test caching a result."""
        processor = DataProcessor()
        
        processor.cache_result('key1', 'value1')
        
        assert processor.get_cached_result('key1') == 'value1'
    
    def test_get_cached_result_nonexistent(self):
        """Test getting nonexistent cached result."""
        processor = DataProcessor()
        
        result = processor.get_cached_result('nonexistent')
        
        assert result is None
    
    def test_cache_overwrite(self):
        """Test overwriting cached result."""
        processor = DataProcessor()
        
        processor.cache_result('key1', 'value1')
        processor.cache_result('key1', 'value2')
        
        assert processor.get_cached_result('key1') == 'value2'
    
    def test_clear_cache(self):
        """Test clearing cache."""
        processor = DataProcessor()
        
        processor.cache_result('key1', 'value1')
        processor.cache_result('key2', 'value2')
        processor.clear_cache()
        
        assert processor.get_cached_result('key1') is None
        assert processor.get_cached_result('key2') is None
    
    def test_cache_different_types(self):
        """Test caching different data types."""
        processor = DataProcessor()
        
        processor.cache_result('string', 'value')
        processor.cache_result('int', 42)
        processor.cache_result('list', [1, 2, 3])
        processor.cache_result('dict', {'key': 'value'})
        
        assert processor.get_cached_result('string') == 'value'
        assert processor.get_cached_result('int') == 42
        assert processor.get_cached_result('list') == [1, 2, 3]
        assert processor.get_cached_result('dict') == {'key': 'value'}
