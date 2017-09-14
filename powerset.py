import sys

length = len(sys.argv) -1 

# for i in range(length):
# 	print(sys.argv[i+1])
# 	for j in range(length):
# 		print(sys.argv[i+1] + sys.argv[j+1])

for i in range(length):
	result = ""
	for j in range(length):
		result = result + sys.argv[((length-1-j + i) % length)+1]
	print result