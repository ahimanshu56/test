"""
Comprehensive tests for data_processor module to achieve high coverage.
"""
import pytest
from src.data_processor import DataProcessor


class TestCalculateStatistics:
    """Test calculate_statistics method."""
    
    def test_calculate_statistics_normal(self):
        """Test with normal list of numbers."""
        processor = DataProcessor()
        stats = processor.calculate_statistics([1, 2, 3, 4, 5])
        
        assert stats["mean"] == 3.0
        assert stats["median"] == 3
        assert stats["min"] == 1
        assert stats["max"] == 5
        assert stats["count"] == 5
        assert stats["stdev"] > 0
    
    def test_calculate_statistics_single_value(self):
        """Test with single value."""
        processor = DataProcessor()
        stats = processor.calculate_statistics([5])
        
        assert stats["mean"] == 5.0
        assert stats["median"] == 5
        assert stats["min"] == 5
        assert stats["max"] == 5
        assert stats["count"] == 1
        assert stats["stdev"] == 0.0
    
    def test_calculate_statistics_empty_list(self):
        """Test with empty list."""
        processor = DataProcessor()
        with pytest.raises(ValueError, match="empty list"):
            processor.calculate_statistics([])
    
    def test_calculate_statistics_non_numeric(self):
        """Test with non-numeric values."""
        processor = DataProcessor()
        with pytest.raises(TypeError, match="must be numbers"):
            processor.calculate_statistics([1, 2, "three"])
    
    def test_calculate_statistics_floats(self):
        """Test with float values."""
        processor = DataProcessor()
        stats = processor.calculate_statistics([1.5, 2.5, 3.5])
        
        assert stats["mean"] == 2.5
        assert stats["count"] == 3


class TestFilterOutliers:
    """Test filter_outliers method."""
    
    def test_filter_outliers_with_outliers(self):
        """Test filtering with actual outliers."""
        processor = DataProcessor()
        numbers = [1, 2, 3, 4, 5, 100]  # 100 is an outlier
        
        filtered = processor.filter_outliers(numbers, threshold=2.0)
        assert 100 not in filtered
        assert len(filtered) < len(numbers)
    
    def test_filter_outliers_no_outliers(self):
        """Test filtering with no outliers."""
        processor = DataProcessor()
        numbers = [1, 2, 3, 4, 5]
        
        filtered = processor.filter_outliers(numbers)
        assert len(filtered) == len(numbers)
    
    def test_filter_outliers_empty_list(self):
        """Test filtering empty list."""
        processor = DataProcessor()
        filtered = processor.filter_outliers([])
        assert filtered == []
    
    def test_filter_outliers_small_list(self):
        """Test filtering list with less than 3 elements."""
        processor = DataProcessor()
        numbers = [1, 2]
        filtered = processor.filter_outliers(numbers)
        assert filtered == numbers
    
    def test_filter_outliers_zero_stdev(self):
        """Test filtering when all values are the same."""
        processor = DataProcessor()
        numbers = [5, 5, 5, 5]
        filtered = processor.filter_outliers(numbers)
        assert filtered == numbers


class TestNormalizeData:
    """Test normalize_data method."""
    
    def test_normalize_data_default_range(self):
        """Test normalization to default 0-1 range."""
        processor = DataProcessor()
        numbers = [0, 50, 100]
        
        normalized = processor.normalize_data(numbers)
        assert normalized[0] == 0.0
        assert normalized[1] == 0.5
        assert normalized[2] == 1.0
    
    def test_normalize_data_custom_range(self):
        """Test normalization to custom range."""
        processor = DataProcessor()
        numbers = [0, 50, 100]
        
        normalized = processor.normalize_data(numbers, min_val=-1.0, max_val=1.0)
        assert normalized[0] == -1.0
        assert normalized[1] == 0.0
        assert normalized[2] == 1.0
    
    def test_normalize_data_empty_list(self):
        """Test normalizing empty list."""
        processor = DataProcessor()
        normalized = processor.normalize_data([])
        assert normalized == []
    
    def test_normalize_data_invalid_range(self):
        """Test with invalid range."""
        processor = DataProcessor()
        with pytest.raises(ValueError, match="min_val must be less than max_val"):
            processor.normalize_data([1, 2, 3], min_val=1.0, max_val=0.0)
    
    def test_normalize_data_same_values(self):
        """Test normalizing when all values are the same."""
        processor = DataProcessor()
        numbers = [5, 5, 5]
        
        normalized = processor.normalize_data(numbers)
        assert all(n == 0.5 for n in normalized)


class TestGroupByRange:
    """Test group_by_range method."""
    
    def test_group_by_range_normal(self):
        """Test grouping with normal data."""
        processor = DataProcessor()
        numbers = [1, 5, 11, 15, 21]
        
        groups = processor.group_by_range(numbers, 10)
        assert "0.0-10.0" in groups
        assert "10.0-20.0" in groups
        assert "20.0-30.0" in groups
    
    def test_group_by_range_empty_list(self):
        """Test grouping empty list."""
        processor = DataProcessor()
        groups = processor.group_by_range([], 10)
        assert groups == {}
    
    def test_group_by_range_invalid_range_size(self):
        """Test with invalid range size."""
        processor = DataProcessor()
        with pytest.raises(ValueError, match="must be positive"):
            processor.group_by_range([1, 2, 3], 0)
        
        with pytest.raises(ValueError, match="must be positive"):
            processor.group_by_range([1, 2, 3], -5)
    
    def test_group_by_range_single_group(self):
        """Test when all numbers fall in one group."""
        processor = DataProcessor()
        numbers = [1, 2, 3, 4]
        
        groups = processor.group_by_range(numbers, 10)
        assert len(groups) == 1


class TestTransformData:
    """Test transform_data method."""
    
    def test_transform_data_sum(self):
        """Test sum operation."""
        processor = DataProcessor()
        data = [{"value": 10}, {"value": 20}, {"value": 30}]
        
        result = processor.transform_data(data, "value", "sum")
        assert result == [60]
    
    def test_transform_data_count(self):
        """Test count operation."""
        processor = DataProcessor()
        data = [{"value": 10}, {"value": 20}, {"value": 30}]
        
        result = processor.transform_data(data, "value", "count")
        assert result == [3]
    
    def test_transform_data_avg(self):
        """Test average operation."""
        processor = DataProcessor()
        data = [{"value": 10}, {"value": 20}, {"value": 30}]
        
        result = processor.transform_data(data, "value", "avg")
        assert result == [20.0]
    
    def test_transform_data_max(self):
        """Test max operation."""
        processor = DataProcessor()
        data = [{"value": 10}, {"value": 20}, {"value": 30}]
        
        result = processor.transform_data(data, "value", "max")
        assert result == [30]
    
    def test_transform_data_min(self):
        """Test min operation."""
        processor = DataProcessor()
        data = [{"value": 10}, {"value": 20}, {"value": 30}]
        
        result = processor.transform_data(data, "value", "min")
        assert result == [10]
    
    def test_transform_data_list(self):
        """Test list operation."""
        processor = DataProcessor()
        data = [{"value": 10}, {"value": 20}, {"value": 30}]
        
        result = processor.transform_data(data, "value", "list")
        assert result == [10, 20, 30]
    
    def test_transform_data_empty_list(self):
        """Test with empty data list."""
        processor = DataProcessor()
        result = processor.transform_data([], "value", "sum")
        assert result == []
    
    def test_transform_data_invalid_operation(self):
        """Test with invalid operation."""
        processor = DataProcessor()
        data = [{"value": 10}]
        
        with pytest.raises(ValueError, match="Unsupported operation"):
            processor.transform_data(data, "value", "invalid")
    
    def test_transform_data_missing_key(self):
        """Test when key is missing from some items."""
        processor = DataProcessor()
        data = [{"value": 10}, {"other": 20}, {"value": 30}]
        
        result = processor.transform_data(data, "value", "list")
        assert result == [10, 30]
    
    def test_transform_data_non_dict_items(self):
        """Test with non-dictionary items."""
        processor = DataProcessor()
        data = [{"value": 10}, "not a dict", {"value": 30}]
        
        result = processor.transform_data(data, "value", "list")
        assert result == [10, 30]
    
    def test_transform_data_avg_no_numeric(self):
        """Test average with no numeric values."""
        processor = DataProcessor()
        data = [{"value": "text"}]
        
        result = processor.transform_data(data, "value", "avg")
        assert result == []


class TestMergeDatasets:
    """Test merge_datasets method."""
    
    def test_merge_datasets_normal(self):
        """Test merging two datasets."""
        processor = DataProcessor()
        dataset1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        dataset2 = [{"id": 1, "age": 30}, {"id": 2, "age": 25}]
        
        merged = processor.merge_datasets(dataset1, dataset2, "id")
        assert len(merged) == 2
        assert merged[0]["name"] == "Alice"
        assert merged[0]["age"] == 30
    
    def test_merge_datasets_both_empty(self):
        """Test merging two empty datasets."""
        processor = DataProcessor()
        merged = processor.merge_datasets([], [], "id")
        assert merged == []
    
    def test_merge_datasets_first_empty(self):
        """Test merging when first dataset is empty."""
        processor = DataProcessor()
        dataset2 = [{"id": 1, "age": 30}]
        
        merged = processor.merge_datasets([], dataset2, "id")
        assert merged == dataset2
    
    def test_merge_datasets_second_empty(self):
        """Test merging when second dataset is empty."""
        processor = DataProcessor()
        dataset1 = [{"id": 1, "name": "Alice"}]
        
        merged = processor.merge_datasets(dataset1, [], "id")
        assert len(merged) == 1
        assert merged[0]["name"] == "Alice"
    
    def test_merge_datasets_no_match(self):
        """Test merging when keys don't match."""
        processor = DataProcessor()
        dataset1 = [{"id": 1, "name": "Alice"}]
        dataset2 = [{"id": 2, "age": 30}]
        
        merged = processor.merge_datasets(dataset1, dataset2, "id")
        assert len(merged) == 1
        assert "age" not in merged[0]
    
    def test_merge_datasets_missing_key(self):
        """Test merging when key is missing from some items."""
        processor = DataProcessor()
        dataset1 = [{"id": 1, "name": "Alice"}, {"name": "Bob"}]
        dataset2 = [{"id": 1, "age": 30}]
        
        merged = processor.merge_datasets(dataset1, dataset2, "id")
        assert len(merged) == 2
