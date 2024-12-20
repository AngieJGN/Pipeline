import pytest
from app import NutritionCalculator

@pytest.fixture
def calculator():
    return NutritionCalculator()

def test_calories_burned(calculator):
    assert calculator.calories_burned(70, 30, 0.05) == 105.0  # Calories
    with pytest.raises(ValueError):
        calculator.calories_burned(-70, 30, 0.05)

def test_total_calories(calculator):
    assert calculator.total_calories(100, 50, 20) == 930  # Calories
    with pytest.raises(ValueError):
        calculator.total_calories(-100, 50, 20)

def test_calorie_deficit(calculator):
    assert calculator.calorie_deficit(2000, 600) == 1400  # Calories
    with pytest.raises(ValueError):
        calculator.calorie_deficit(2000,-600)