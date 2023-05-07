import pytest
from plates import is_valid

def test_valid():
    assert is_valid("ABCDE4") == True
    assert is_valid("CS50") == True

def test_punctuation():
    assert is_valid("AB.CD") == False
    assert is_valid("AB?C") == False
    assert is_valid("AB,C") == False
    assert is_valid("AB!C") == False

def test_numbers_in_middle():
    assert is_valid("AB3D") == False
    assert is_valid("3D3D") == False

def test__zero_first():
    assert is_valid("AB02") == False

def test_lenght():
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False

def test_letters_first():
    assert is_valid("12DEF") == False
    assert is_valid("A222") == False
