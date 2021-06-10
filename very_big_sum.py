def user_int():
	user_int = []
	for i in range(2):
		inputs = input().split()
		if len(inputs) > 1:
			user_int.append(inputs)
	return user_int

# Use list comprehensive to convert string to integers
converts = sum([sum([int(number) for number in new]) for new in user_int()])


print(converts)