import pytest
from working import convert

def test_convert_valid_colon():
    assert convert("10:30 AM to 12:00 PM") == "10:30 to 12:00"
    assert convert("12:00 PM to 10:30 AM") == "12:00 to 10:30"

def test_convert_valid_none():
    assert convert("8 AM to 9 PM") == "08:00 to 21:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert_invalid_hour():
    with pytest.raises(ValueError):
        convert("13:00 AM to 12:00 PM")

def test_convert_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:65 AM to 12:00 PM")

def test_nonsense():
    with pytest.raises(ValueError):
        convert("you undeREstimate my power!")

