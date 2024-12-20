import numpy as np

class SolarCalculator:
    def energy_generated(self, solar_panel_area, efficiency, sunlight_hours):
        if solar_panel_area <= 0 or efficiency <= 0 or sunlight_hours <= 0:
            raise ValueError("All input values must be positive.")
        return solar_panel_area * efficiency * sunlight_hours * 1000  # Energy in Wh

    def cost_per_watt(self, total_cost, watts):
        if total_cost <= 0 or watts <= 0:
            raise ValueError("Total cost and watts must be positive values.")
        return total_cost / watts

    def charging_time(self, battery_capacity, charging_power):
        if battery_capacity <= 0 or charging_power <= 0:
            raise ValueError("Battery capacity and charging power must be positive values.")
        return battery_capacity / charging_power  # Time in hours

    def panel_efficiency_drop(self, initial_efficiency, years, degradation_rate):
        if initial_efficiency <= 0 or years < 0 or degradation_rate < 0:
            raise ValueError("Efficiency must be positive, and years/degradation rate must be non-negative.")
        return initial_efficiency * ((1 - degradation_rate) ** years)

if __name__ == "_main_":
    calculator = SolarCalculator()
    print("Energy generated (10m², 0.2 efficiency, 5 hours):", calculator.energy_generated(10, 0.2, 5), "Wh")
    print("Cost per watt ($500, 250 watts):", calculator.cost_per_watt(500, 250), "$/W")
    print("Charging time (1000 Wh battery, 200 W charging):", calculator.charging_time(1000, 200), "hours")
    print("Efficiency after 5 years (0.2 initial, 0.02 degradation rate):", 
          calculator.panel_efficiency_drop(0.2,5,0.02))