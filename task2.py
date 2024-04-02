while True:
  try:
    original_servings = float(input("How many servings does the recipe originally make? "))

    desired_servings = float(input("How many servings would you like to make? "))
    
    break
  except ValueError:
    print("Invalid input. Please enter numbers for the number of servings.")

try:
  adjustment_factor = desired_servings / original_servings
except ZeroDivisionError:
  print("Error: Cannot divide by zero. Please enter a valid number of original servings.")
else:
  print(f"The adjustment factor is: {adjustment_factor:.2f}")

  recipe = {"ingredient1": 1.5, "ingredient2": 2.0, "ingredient3": 0.75}
  for ingredient, quantity in recipe.items():
    adjusted_quantity = quantity * adjustment_factor
    print(f"- {adjusted_quantity:.2f} {ingredient}")

finally:
  print("Enjoy your cooking!")