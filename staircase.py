loop = int(input("enter a number: "))

for i in range(loop):
	print((" " * (loop - (i+1))) + ("#" * (i+1)))
