import pytest
import ast
import importlib
import array as arr

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Tests for search_array function
def test_search_array_found():
    from assignment import search_array
    result = search_array(44)
    expected = 1  # Assuming the first occurrence of 44 is at index 1
    assert result == expected, f"DMACC Student, the function 'search_array' did not return the expected index for value 44.\nExpected: {expected}\nActual: {result}\nPlease check your search logic."

def test_search_array_not_found():
    from assignment import search_array
    result = search_array(100)
    expected = -1
    assert result == expected, f"DMACC Student, the function 'search_array' did not return the expected value for a non-existent value 100.\nExpected: {expected}\nActual: {result}\nPlease check your search logic."

# Tests for sort_array function
def test_sort_array():
    from assignment import sort_array, hardcoded_array
    returned_array = sort_array()
    if returned_array != None:
        hardcoded_array = returned_array
    expected = arr.array('i', [22, 23, 26, 44, 44, 63, 99])
    assert hardcoded_array == expected, f"DMACC Student, the function 'sort_array' did not sort the array as expected.\nExpected: {expected}\nActual: {hardcoded_array}\nPlease check your sorting logic."

if __name__ == "__main__":
    pytest.main()