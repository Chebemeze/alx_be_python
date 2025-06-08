def perform_operation(num1, num2, operation):

  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    if num1 == 0 or num2 == 0:
      return ("Cannot divide by zero. Kindly provide nonzero values")
    else:
      return num1 - num2