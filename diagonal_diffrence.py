arr = []
user = ''
lenght = 0

def appending():
	global user
	lenght = len(user)
	convert = [int(number) for number in user]
	arr.append(convert)

	for i in range(lenght - 1):
		user = input().split()
		convert = [int(number) for number in user]
		arr.append(convert)

while True:
	user = input().split()
	if len(user) > 1:
		appending()
		break
	else:
		continue

left = 0
right = 0

for i in range(len(arr)):
	left += arr[i][-i - 1]

for i in range(len(arr)):
	right += arr[i][i]
result = abs(right - left)
print(result)