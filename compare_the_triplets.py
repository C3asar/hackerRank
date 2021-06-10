# Use a function to get the user inputs
def records():
	user_int = []
	for i in range(2):
		# user_int.append(input("Enter the first record:\n").split())
		user_int.append(input().split())
		
	# user_int = [int(number for number in user_int)]
	return user_int


# Use comprehensive list to convert strings to integers
records = [[int(number) for number in new] for new in records()]

bob = int()
alice = int()

for i in range(len(records[0])):
	if (records[0][i] < records[1][i]) == True:
		# print(records[1][i], '>', records[0][i])
		bob += 1
	elif (records[0][i] > records[1][i]) == True:
		# print(records[0][i], '>', records[1][i])
		alice += 1
	elif (records[1][i] == records[0][i]) == True:
		# print(records[1][i], '==', records[0][i])
		continue
		
print(alice, bob)