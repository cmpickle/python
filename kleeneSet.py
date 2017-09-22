from itertools import permutations, combinations_with_replacement
import sys

inputs = sys.argv[1:]
result = list("")

for i in range(len(inputs)):
	for j in range(len(inputs)):
		result.append(list(combinations_with_replacement(inputs, 3)))

print result