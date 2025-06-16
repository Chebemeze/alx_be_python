def safe_divide(numerator, denominator):
  try:
    num = float(numerator)
    denom = float(denominator)
  except ValueError:
    return("Error: Please enter numeric values only.")

  try:
    result = num / denom
    a = f"The result of the division is {result}"
    return(a)
  except ZeroDivisionError:
    return("Error: Cannot divide by zero.")