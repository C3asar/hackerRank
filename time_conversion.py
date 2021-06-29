user_int = input()

unit = user_int[-2:]

time = [number for number in user_int[:-2].split(":")]


if time[0] == '12' and ((unit == 'PM' and time[1] == '00') or unit == 'AM') :
	time[0] = '00'
elif unit == 'PM' and int(time[0]) == 12 and int(time[2]) > 0:
	time = time
elif unit == 'PM':
	time[0] = str(int(time[0]) + 12)
print(f"{time[0]}:{time[1]}:{time[2]}")