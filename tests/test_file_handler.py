"""Comprehensive tests for file_handler module."""
import pytest
import os
import json
import tempfile
import shutil
from src.file_handler import FileHandler


class TestFileHandler:
    """Test FileHandler class."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for tests."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir, ignore_errors=True)
    
    @pytest.fixture
    def temp_file(self, temp_dir):
        """Create a temporary file for tests."""
        filepath = os.path.join(temp_dir, "test_file.txt")
        with open(filepath, 'w') as f:
            f.write("Test content")
        return filepath
    
    def test_read_file_success(self, temp_file):
        """Test reading a file successfully."""
        content = FileHandler.read_file(temp_file)
        assert content == "Test content"
    
    def test_read_file_not_found(self):
        """Test reading non-existent file raises error."""
        with pytest.raises(FileNotFoundError, match="File not found"):
            FileHandler.read_file("/nonexistent/file.txt")
    
    def test_write_file_success(self, temp_dir):
        """Test writing to a file successfully."""
        filepath = os.path.join(temp_dir, "new_file.txt")
        result = FileHandler.write_file(filepath, "New content")
        
        assert result is True
        assert os.path.exists(filepath)
        
        with open(filepath, 'r') as f:
            assert f.read() == "New content"
    
    def test_write_file_creates_directory(self, temp_dir):
        """Test writing file creates parent directories."""
        filepath = os.path.join(temp_dir, "subdir", "new_file.txt")
        result = FileHandler.write_file(filepath, "Content")
        
        assert result is True
        assert os.path.exists(filepath)
    
    def test_write_file_overwrites_existing(self, temp_file):
        """Test writing to existing file overwrites it."""
        result = FileHandler.write_file(temp_file, "Overwritten")
        
        assert result is True
        with open(temp_file, 'r') as f:
            assert f.read() == "Overwritten"
    
    def test_append_to_file_success(self, temp_file):
        """Test appending to a file successfully."""
        result = FileHandler.append_to_file(temp_file, " appended")
        
        assert result is True
        with open(temp_file, 'r') as f:
            assert f.read() == "Test content appended"
    
    def test_append_to_file_creates_new(self, temp_dir):
        """Test appending creates new file if not exists."""
        filepath = os.path.join(temp_dir, "append_file.txt")
        result = FileHandler.append_to_file(filepath, "New content")
        
        assert result is True
        assert os.path.exists(filepath)
    
    def test_read_json_success(self, temp_dir):
        """Test reading JSON file successfully."""
        filepath = os.path.join(temp_dir, "test.json")
        test_data = {"name": "John", "age": 30}
        
        with open(filepath, 'w') as f:
            json.dump(test_data, f)
        
        result = FileHandler.read_json(filepath)
        assert result == test_data
    
    def test_read_json_not_found(self):
        """Test reading non-existent JSON file raises error."""
        with pytest.raises(FileNotFoundError, match="File not found"):
            FileHandler.read_json("/nonexistent/file.json")
    
    def test_write_json_success(self, temp_dir):
        """Test writing JSON file successfully."""
        filepath = os.path.join(temp_dir, "output.json")
        test_data = {"name": "Jane", "age": 25, "active": True}
        
        result = FileHandler.write_json(filepath, test_data)
        
        assert result is True
        assert os.path.exists(filepath)
        
        with open(filepath, 'r') as f:
            loaded_data = json.load(f)
            assert loaded_data == test_data
    
    def test_write_json_creates_directory(self, temp_dir):
        """Test writing JSON creates parent directories."""
        filepath = os.path.join(temp_dir, "subdir", "data.json")
        result = FileHandler.write_json(filepath, {"key": "value"})
        
        assert result is True
        assert os.path.exists(filepath)
    
    def test_file_exists_true(self, temp_file):
        """Test file_exists returns True for existing file."""
        assert FileHandler.file_exists(temp_file) is True
    
    def test_file_exists_false(self):
        """Test file_exists returns False for non-existent file."""
        assert FileHandler.file_exists("/nonexistent/file.txt") is False
    
    def test_file_exists_directory(self, temp_dir):
        """Test file_exists returns False for directory."""
        assert FileHandler.file_exists(temp_dir) is False
    
    def test_get_file_size(self, temp_file):
        """Test getting file size."""
        size = FileHandler.get_file_size(temp_file)
        assert size == len("Test content")
    
    def test_get_file_size_not_found(self):
        """Test getting size of non-existent file raises error."""
        with pytest.raises(FileNotFoundError, match="File not found"):
            FileHandler.get_file_size("/nonexistent/file.txt")
    
    def test_list_files_all(self, temp_dir):
        """Test listing all files in directory."""
        # Create test files
        open(os.path.join(temp_dir, "file1.txt"), 'w').close()
        open(os.path.join(temp_dir, "file2.py"), 'w').close()
        open(os.path.join(temp_dir, "file3.txt"), 'w').close()
        
        files = FileHandler.list_files(temp_dir)
        assert len(files) == 3
        assert "file1.txt" in files
        assert "file2.py" in files
        assert "file3.txt" in files
    
    def test_list_files_with_extension(self, temp_dir):
        """Test listing files filtered by extension."""
        open(os.path.join(temp_dir, "file1.txt"), 'w').close()
        open(os.path.join(temp_dir, "file2.py"), 'w').close()
        open(os.path.join(temp_dir, "file3.txt"), 'w').close()
        
        files = FileHandler.list_files(temp_dir, extension=".txt")
        assert len(files) == 2
        assert "file1.txt" in files
        assert "file3.txt" in files
        assert "file2.py" not in files
    
    def test_list_files_empty_directory(self, temp_dir):
        """Test listing files in empty directory."""
        files = FileHandler.list_files(temp_dir)
        assert len(files) == 0
    
    def test_list_files_not_found(self):
        """Test listing files in non-existent directory raises error."""
        with pytest.raises(FileNotFoundError, match="Directory not found"):
            FileHandler.list_files("/nonexistent/directory")
    
    def test_list_files_ignores_subdirectories(self, temp_dir):
        """Test listing files ignores subdirectories."""
        open(os.path.join(temp_dir, "file.txt"), 'w').close()
        os.makedirs(os.path.join(temp_dir, "subdir"))
        
        files = FileHandler.list_files(temp_dir)
        assert len(files) == 1
        assert "file.txt" in files
    
    def test_list_files_sorted(self, temp_dir):
        """Test listing files returns sorted results."""
        open(os.path.join(temp_dir, "c.txt"), 'w').close()
        open(os.path.join(temp_dir, "a.txt"), 'w').close()
        open(os.path.join(temp_dir, "b.txt"), 'w').close()
        
        files = FileHandler.list_files(temp_dir)
        assert files == ["a.txt", "b.txt", "c.txt"]
    
    def test_delete_file_success(self, temp_file):
        """Test deleting a file successfully."""
        result = FileHandler.delete_file(temp_file)
        
        assert result is True
        assert not os.path.exists(temp_file)
    
    def test_delete_file_not_exists(self):
        """Test deleting non-existent file returns False."""
        result = FileHandler.delete_file("/nonexistent/file.txt")
        assert result is False
