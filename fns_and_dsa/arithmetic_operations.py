def perform_operation(num1, num2, operation):

  op_list = ["add", "subtract", "multiply", "divide"]
 
  for i in range(0,4):

    if op_list[i] == operation:
      if op_list[i] == "add":
        return num1 + num2
      elif op_list[i] == "subtract":
        return num1 - num2
      elif op_list[i] == "multiply":
        return num1 * num2
      elif op_list[i] == "divide":
          if num1 == 0 or num2 == 0:
            return ("Cannot divide by zero. Kindly provide nonzero values")
          else:
            return num1 - num2 




