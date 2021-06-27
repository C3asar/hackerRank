zero = 0
positive = 0
negative = 0

if int(input()) > 1:
	array = [int(number) for number in input().split()]

	for element in array:
		if element == 0:
			zero += 1
		elif element > 0:
			positive += 1
		elif element < 0:
			negative += 1
	result = [positive, negative, zero]

	result = [number / len(array) for number in result]
	result = [print(format(number, '.6f')) for number in result]
