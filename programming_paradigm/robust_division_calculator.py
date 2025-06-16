def safe_divide(numerator, denominator):
  try:
    num = float(numerator)
    denom = float(denominator)
  except ValueError:
    return("Kindly enter two valid numbers not strings!")

  try:
    result = num / denom
    return(f"The result of the division is {result}")
  except ZeroDivisionError:
    return("Error. Cannot divide by zero.")
  except TypeError:
    return("Error: Please enter numeric values only.")