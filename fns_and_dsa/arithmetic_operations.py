def perform_operation(num1, num2, operations):

  if operations == "+":
    return num1 + num2
  elif operations == "-":
    return num1 - num2
  elif operations == "*":
    return num1 * num2
  elif operations == "/":
    if num1 == 0 or num2 == 0:
      return ("Cannot divide by zero. Kindly provide nonzero values")
    else:
      return num1 - num2