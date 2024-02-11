import pytest

def add_numbers(a, b) -> float:
    for num in [a, b]:
        if not isinstance(num, float | int):
            return 0
        
    return a + b 

class TestGroup:
    def test_one_plus_one_is_two(self):
        a, b = 1, 1   # Arrange
        actual = add_numbers(a, b)  # Act
        expected = 2 
        
        assert actual == expected   # Assert
        
        
    def test_one_plus_letter_returns_zero(self):
        a, b = 1, 'z'
        actual = add_numbers(a, b)
        expected = 0
        
        assert actual == expected