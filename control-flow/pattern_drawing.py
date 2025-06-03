pattern_size = int(input("Enter the size of the pattern: "))

i = 0

if pattern_size >= 0:
	while i < pattern_size:
		for j in range(1,5):
			print("*", end="")
		print()
		i +=1
else:
	print("Enter a positive number next time!")