loop = int(input())

arr = []
new_arr = []

for i in range(loop):
	arr.append(int(input()))


for i in arr:
	if i < 38:
		new_arr.append(i)
	else:
		for j in range(i, 101):
			if j % 5 == 0:
				diff = j - i
				if diff < 3:
					new_arr.append(j)
					break
				else:
					new_arr.append(i)
					break


for i in new_arr:
	print(i)