
import sys
from os import path

TEST = 't' in sys.argv or '-t' in sys.argv
VERBOSE = 'v' in sys.argv or '-v' in sys.argv
directory = path.dirname(path.abspath(__file__))
path = path.join(directory, 'test') if TEST else path.join(directory, 'input')
with open(path, 'r') as f:
	line = f.readline()


for index, c in enumerate(line):
	if index >= 4:
		if len(set(line[index - 4: index])) == 4:
			if VERBOSE:
				print(set(line[index - 4: index]))
			break

print(f'End of marker index: {index}')

