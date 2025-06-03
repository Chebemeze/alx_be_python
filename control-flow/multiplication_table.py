users_input = int(input("Enter a number to see its multiplication table: "))

for i in range(1,11):
	product = users_input * i
	print(f"{users_input} * {i} = {product}")