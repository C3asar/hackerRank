# Use a comprehesion list to set the rows(m) columns(n) rotation factorial(r)' values
m, n, r = [int(number) for number in input().split()]
count = 0
arr = []

# while loop until the count == colmns(n) times 
while count != n:
	# comprehension list & append the result to an arr = 2D list
	user_int = [int(number) for number in input().split()]
	# Check if user input == rows len
	if len(user_int) == m:
		arr.append(user_int)
		count += 1
	else:
		continue

print(arr)