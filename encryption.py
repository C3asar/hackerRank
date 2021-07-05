import math
user_int = input().replace(" ", "")
length = len(user_int)
sqrt = math.sqrt(length)
ceil = math.ceil(sqrt)
floor = math.floor(sqrt)
mult = floor * ceil
slice_one = 0
slice_two = ceil
arr = []
encry_string = []

if mult > length:
	diffrence = mult - length
	new_string = user_int + (diffrence * " ")
	for i in range(floor):
		arr.append((new_string[slice_one:slice_two]))
		slice_two += ceil
		slice_one += ceil
	for i in range(ceil):
		result = ''
		for j in range(floor):
			result += arr[j][i]
		encry_string.append(result)
	encry_string = [word.strip() for word in encry_string]
	print(" ".join(encry_string))




elif mult < length:
	mult = ceil * ceil
	diffrence = mult - length
	new_string = user_int + (diffrence * " ")
	for i in range(ceil):
		arr.append((new_string[slice_one:slice_two]))
		slice_two += ceil
		slice_one += ceil
	for i in range(ceil):
		result = ''
		for j in range(ceil):
			result += arr[j][i]
		encry_string.append(result)
	encry_string = [word.strip() for word in encry_string]
	print(" ".join(encry_string))

elif mult == length:
	new_string = user_int
	for i in range(floor):
		arr.append((new_string[slice_one:slice_two]))
		slice_two += ceil
		slice_one += ceil
	for i in range(ceil):
		result = ''
		for j in range(floor):
			result += arr[j][i]
		encry_string.append(result)
	encry_string = [word.strip() for word in encry_string]
	print(" ".join(encry_string))
 