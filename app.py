
class NutritionCalculator:
    def calories_burned(self, weight, activity_minutes, calories_per_kg_per_minute):
        if weight <= 0 or activity_minutes <= 0 or calories_per_kg_per_minute <= 0:
            raise ValueError("All input values must be positive.")
        return weight * activity_minutes * calories_per_kg_per_minute

    def total_calories(self, carbs, proteins, fats):
        if carbs < 0 or proteins < 0 or fats < 0:
            raise ValueError("Nutrient values cannot be negative.")
        return (carbs * 4) + (proteins * 4) + (fats * 9)

    def calorie_deficit(self, calories_consumed, calories_burned):
        if calories_consumed < 0 or calories_burned < 0:
            raise ValueError("Calories cannot be negative.")
        return calories_consumed - calories_burned

if __name__== "_main_":
    calculator = NutritionCalculator()
    print("Calories burned (70kg, 30 minutes, 0.05 cal/kg/min):", calculator.calories_burned(70, 30, 0.05), "cal")
    print("Total calories (100g carbs, 50g proteins, 20g fats):", calculator.total_calories(100, 50, 20), "cal")
    print("Calorie deficit (2000 consumed, 600 burned):", calculator.calorie_deficit(2000, 600),"cal")