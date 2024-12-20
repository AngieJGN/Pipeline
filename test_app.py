import pytest
from app import SolarCalculator

@pytest.fixture
def calculator():
    return SolarCalculator()

def test_energy_generated(calculator):
    assert calculator.energy_generated(10, 0.2, 5) == 10000  # Wh
    with pytest.raises(ValueError):
        calculator.energy_generated(-10, 0.2, 5)

def test_cost_per_watt(calculator):
    assert calculator.cost_per_watt(500, 250) == 2  # $/W
    with pytest.raises(ValueError):
        calculator.cost_per_watt(500, 0)

def test_charging_time(calculator):
    assert calculator.charging_time(1000, 200) == 5  # Hours
    with pytest.raises(ValueError):
        calculator.charging_time(1000, -200)

def test_panel_efficiency_drop(calculator):
    assert pytest.approx(calculator.panel_efficiency_drop(0.2, 5, 0.02), 0.0001) == 0.18048
    with pytest.raises(ValueError):
        calculator.panel_efficiency_drop(-0.2, 5, 0.02)