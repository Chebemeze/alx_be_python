number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
	case "+":
		addition = number1 + number2
		print(f"The result is {addition}.")
		
	case "-":
		subtract = number1 - number2
		print(f"The result is {subtract}.")
		
	case "*":
		multiply = number1 * number2
		print(f"The result is {multiply}.")
		
	case "/":
		if number1 == 0 or number2 == 0:
			print(f"Cannot divide by zero.")
		else:
			divide = int(number1 / number2)
			print(f"The result is {divide}.")
			
	case _:
		print("Invalid operator. Provide a valid operator (+, -, *, /).")