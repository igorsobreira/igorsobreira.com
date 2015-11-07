import pytest

def miles_to_km(miles):
    return miles * 1.60934

def test_miles_to_km_one():
    assert miles_to_km(1) == 1.60934

def test_miles_to_km_zero():
    assert miles_to_km(0) == 0

def test_miles_to_km_other():
    assert miles_to_km(42) == 67.59228

@pytest.mark.parametrize('value', [
    'ten',
    None,
    [1,2,3],
])
def test_miles_to_km_invalid_arguments(value):
    with pytest.raises(TypeError):
        miles_to_km(value)
