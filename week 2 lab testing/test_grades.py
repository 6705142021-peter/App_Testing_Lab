from grades import letter_grade
import pytest

def test_boundary_A_grade():
    assert letter_grade(80) == "A"
    assert letter_grade(79) == "B"

def test_boundary_B_grade():
    assert letter_grade(70) == "B"
    assert letter_grade(69) == "C"

def test_boundary_pass_fail():
    assert letter_grade(60) == "C"
    assert letter_grade(59) == "F"

def test_minimum_valid():
    assert letter_grade(0) == "F"

def test_maximum_valid():
    assert letter_grade(100) == "A"

def test_below_minimum_invalid():
    with pytest.raises(ValueError):
        letter_grade(-1)