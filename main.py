
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) > len(num2):
	print ('False')
	sys.exit(0)

size = len(num1)
check = False

if (set(num1).issubset(num2)):
	for i in range(len(num2)):
		for j in range(len(num1)):
			if (num2[i] != num1[j]):
				break
			i += 1
			if (i == len(num1)):
				check = True
	print(check)
else:
	print(check)
