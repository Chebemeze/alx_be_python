FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  celsius_temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return (celsius_temp)

def convert_to_fahrenheit(celsius):
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  fahrenheit_temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return (fahrenheit_temp)

while True:
  try:
    temp = float(input("Enter the temperature to convert: "))
    break
  except ValueError:
    print("Failed to convert, kindly provide a valid number")

temp_degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
match temp_degree:
  case "c":
    converted_temp = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {converted_temp}°F")

  case "f":
    converted_temp = convert_to_celsius(temp)
    print(f"{temp}°F is {converted_temp}°C")
    
  case _:
    print("Enter a valid temperature unit (C/F)")