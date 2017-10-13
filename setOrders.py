from math import factorial
import sys

length = int(sys.argv[1])

result = factorial(length)
for i in range(len(sys.argv)-2):
	result = result/factorial(int(sys.argv[i+2]))

print(str(result))