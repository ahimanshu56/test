"""Comprehensive tests for data_processor module."""
import pytest
from src.data_processor import DataProcessor


class TestDataProcessor:
    """Test DataProcessor class."""
    
    def test_filter_positive_numbers(self):
        """Test filtering positive numbers."""
        result = DataProcessor.filter_positive([1, -2, 3, 0, -5, 7])
        assert result == [1, 3, 7]
    
    def test_filter_positive_empty_list(self):
        """Test filtering positive from empty list."""
        result = DataProcessor.filter_positive([])
        assert result == []
    
    def test_filter_positive_all_negative(self):
        """Test filtering positive when all are negative."""
        result = DataProcessor.filter_positive([-1, -2, -3])
        assert result == []
    
    def test_filter_positive_with_floats(self):
        """Test filtering positive with float numbers."""
        result = DataProcessor.filter_positive([1.5, -2.3, 0.0, 3.7])
        assert result == [1.5, 3.7]
    
    def test_filter_negative_numbers(self):
        """Test filtering negative numbers."""
        result = DataProcessor.filter_negative([1, -2, 3, 0, -5, 7])
        assert result == [-2, -5]
    
    def test_filter_negative_empty_list(self):
        """Test filtering negative from empty list."""
        result = DataProcessor.filter_negative([])
        assert result == []
    
    def test_filter_negative_all_positive(self):
        """Test filtering negative when all are positive."""
        result = DataProcessor.filter_negative([1, 2, 3])
        assert result == []
    
    def test_calculate_mean(self):
        """Test calculating mean."""
        result = DataProcessor.calculate_mean([1, 2, 3, 4, 5])
        assert result == 3.0
    
    def test_calculate_mean_single_value(self):
        """Test calculating mean with single value."""
        result = DataProcessor.calculate_mean([5])
        assert result == 5.0
    
    def test_calculate_mean_empty_list(self):
        """Test calculating mean of empty list raises error."""
        with pytest.raises(ValueError, match="Cannot calculate mean of empty list"):
            DataProcessor.calculate_mean([])
    
    def test_calculate_mean_floats(self):
        """Test calculating mean with floats."""
        result = DataProcessor.calculate_mean([1.5, 2.5, 3.5])
        assert abs(result - 2.5) < 0.0001
    
    def test_calculate_median_odd_count(self):
        """Test calculating median with odd count."""
        result = DataProcessor.calculate_median([1, 3, 5, 7, 9])
        assert result == 5
    
    def test_calculate_median_even_count(self):
        """Test calculating median with even count."""
        result = DataProcessor.calculate_median([1, 2, 3, 4])
        assert result == 2.5
    
    def test_calculate_median_single_value(self):
        """Test calculating median with single value."""
        result = DataProcessor.calculate_median([5])
        assert result == 5
    
    def test_calculate_median_empty_list(self):
        """Test calculating median of empty list raises error."""
        with pytest.raises(ValueError, match="Cannot calculate median of empty list"):
            DataProcessor.calculate_median([])
    
    def test_calculate_std_dev(self):
        """Test calculating standard deviation."""
        result = DataProcessor.calculate_std_dev([2, 4, 4, 4, 5, 5, 7, 9])
        assert abs(result - 2.138) < 0.01
    
    def test_calculate_std_dev_insufficient_data(self):
        """Test calculating std dev with insufficient data."""
        with pytest.raises(ValueError, match="Need at least 2 numbers"):
            DataProcessor.calculate_std_dev([5])
    
    def test_calculate_std_dev_empty_list(self):
        """Test calculating std dev of empty list raises error."""
        with pytest.raises(ValueError, match="Need at least 2 numbers"):
            DataProcessor.calculate_std_dev([])
    
    def test_find_outliers_default_threshold(self):
        """Test finding outliers with default threshold."""
        data = [10, 12, 11, 13, 12, 100, 11, 13]
        outliers = DataProcessor.find_outliers(data)
        assert 100 in outliers
        assert len(outliers) == 1
    
    def test_find_outliers_custom_threshold(self):
        """Test finding outliers with custom threshold."""
        data = [10, 12, 11, 13, 12, 20, 11, 13]
        outliers = DataProcessor.find_outliers(data, threshold=1.5)
        assert 20 in outliers
    
    def test_find_outliers_no_outliers(self):
        """Test finding outliers when none exist."""
        data = [10, 11, 12, 13, 14]
        outliers = DataProcessor.find_outliers(data)
        assert len(outliers) == 0
    
    def test_find_outliers_insufficient_data(self):
        """Test finding outliers with insufficient data."""
        result = DataProcessor.find_outliers([1, 2])
        assert result == []
    
    def test_find_outliers_zero_std_dev(self):
        """Test finding outliers when all values are same."""
        data = [5, 5, 5, 5, 5]
        outliers = DataProcessor.find_outliers(data)
        assert len(outliers) == 0
    
    def test_normalize_numbers(self):
        """Test normalizing numbers."""
        result = DataProcessor.normalize([1, 2, 3, 4, 5])
        assert result[0] == 0.0
        assert result[-1] == 1.0
        assert all(0 <= x <= 1 for x in result)
    
    def test_normalize_empty_list(self):
        """Test normalizing empty list."""
        result = DataProcessor.normalize([])
        assert result == []
    
    def test_normalize_single_value(self):
        """Test normalizing single value."""
        result = DataProcessor.normalize([5])
        assert result == [0.5]
    
    def test_normalize_same_values(self):
        """Test normalizing when all values are same."""
        result = DataProcessor.normalize([5, 5, 5, 5])
        assert all(x == 0.5 for x in result)
    
    def test_normalize_negative_numbers(self):
        """Test normalizing negative numbers."""
        result = DataProcessor.normalize([-10, 0, 10])
        assert result[0] == 0.0
        assert result[1] == 0.5
        assert result[2] == 1.0
    
    def test_group_by_range(self):
        """Test grouping numbers by range."""
        result = DataProcessor.group_by_range([1, 5, 11, 15, 23, 27], 10)
        assert "0-9" in result
        assert "10-19" in result
        assert "20-29" in result
        assert 1 in result["0-9"]
        assert 11 in result["10-19"]
        assert 23 in result["20-29"]
    
    def test_group_by_range_negative_numbers(self):
        """Test grouping negative numbers by range."""
        result = DataProcessor.group_by_range([-5, -15, 5, 15], 10)
        assert len(result) > 0
    
    def test_group_by_range_invalid_size(self):
        """Test grouping with invalid range size."""
        with pytest.raises(ValueError, match="Range size must be positive"):
            DataProcessor.group_by_range([1, 2, 3], 0)
        
        with pytest.raises(ValueError, match="Range size must be positive"):
            DataProcessor.group_by_range([1, 2, 3], -5)
    
    def test_group_by_range_empty_list(self):
        """Test grouping empty list."""
        result = DataProcessor.group_by_range([], 10)
        assert result == {}
    
    def test_remove_duplicates(self):
        """Test removing duplicates."""
        result = DataProcessor.remove_duplicates([1, 2, 2, 3, 1, 4, 3])
        assert result == [1, 2, 3, 4]
    
    def test_remove_duplicates_preserves_order(self):
        """Test that remove_duplicates preserves order."""
        result = DataProcessor.remove_duplicates([3, 1, 2, 1, 3])
        assert result == [3, 1, 2]
    
    def test_remove_duplicates_empty_list(self):
        """Test removing duplicates from empty list."""
        result = DataProcessor.remove_duplicates([])
        assert result == []
    
    def test_remove_duplicates_no_duplicates(self):
        """Test removing duplicates when none exist."""
        result = DataProcessor.remove_duplicates([1, 2, 3, 4])
        assert result == [1, 2, 3, 4]
    
    def test_remove_duplicates_strings(self):
        """Test removing duplicates with strings."""
        result = DataProcessor.remove_duplicates(["a", "b", "a", "c", "b"])
        assert result == ["a", "b", "c"]
