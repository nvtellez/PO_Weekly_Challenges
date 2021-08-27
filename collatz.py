def collatz(numArr):
	lowCount = 2**31-1
	lowCountNum = 0
	for num in numArr:
		count = 0
		tempNum = num
		while (tempNum != 1):
			if (tempNum % 2 == 0):
				tempNum = tempNum // 2
				count += 1
			elif (tempNum % 2 == 1):
				tempNum = tempNum * 3 + 1
				count += 1
			else:
				return 'Enter a positive integer greater than 1.'
		if (count < lowCount):
			lowCount = count
			lowCountNum = num
	index = numArr.index(lowCountNum)
	if (index == 0):
		return 'a'
	else:
		return 'b'

nums = [10,15]
# print('Enter two numbers.')
# for i in range(0, 2):
# 	ele = int(input())
# 	nums.append(ele)
# print(nums)
print(collatz(nums))
