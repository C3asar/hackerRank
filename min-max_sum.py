# arr = [int(number) for number in input("enter number: ").split()]

# smallest = 0
# [smallest := smallest + num for num in arr if num != (max(arr))]

# bigger = 0
# [bigger := bigger + num for num in arr if num != (min(arr))]

# print(smallest, bigger)


# Second solution since HaclerRank is not accepting :=

bigger = 0
smallest = 0
user = input().split()

arr = [int(number) for number in user]

# convert it to strings to check for equality
equal = [number for number in user]

result = equal.count(equal[0]) == len(equal)

if result:
	equal = [int(number) for number in user]
	for i in range(len(equal) - 1):
		bigger += equal[i]
		smallest += equal[i]


else:
	smallest = 0
	for i in arr:
		if i != max(arr):
			smallest += i

	bigger = 0
	for i in arr:
		if i != min(arr):
			bigger += i

print(smallest, bigger)

