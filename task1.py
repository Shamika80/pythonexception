def fahrenheit_to_celsius(fahrenheit):

  try:
    celsius = (fahrenheit - 32) * 5 / 9
  except ZeroDivisionError:
    print("Error: Division by zero occurred during conversion.")
    return 'error'
  else:
    print(f"{fahrenheit:.2f} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")
    return celsius  

  finally:
    print("Thank you for using the weather forecast application!")

temperature_f = 100
temperature_c = fahrenheit_to_celsius(temperature_f)

if temperature_c != 'error':
  max_temp=  input(f"Would you like to convert another temperature? (y/n)")