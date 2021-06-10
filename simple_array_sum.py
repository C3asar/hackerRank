user_int = ''
new = []

while True:
	user_int = input().split(' ')
	if len(user_int) > 1:
	    for i in range(len(user_int)):
	        new.append(int(user_int[i]))	    
	    break
	else:
		continue


print(sum(new))