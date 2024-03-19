import pytest  
from area import calculate_area_square  

# New test added to validate calculations.  
def test_calculate_area_square():  
    assert calculate_area_square(2) == 4  
    assert calculate_area_square(2.5) == 6.25
    assert calculate_area_square(3) == 11
    # Use last two digits of student id for output.
    assert calculate_area_square(99) == 9801
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])
