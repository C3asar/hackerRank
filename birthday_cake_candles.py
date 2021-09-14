def birthdayCakeCandles(candles):
	max_num = max(candles)
	count = 0
	for num in candles:
		if max_num == num:
			count += 1
		else:
			continue
	return count


num_of_candles = int(input())
candles = [int(candle) for candle in input().split()]

print(birthdayCakeCandles(candles))
