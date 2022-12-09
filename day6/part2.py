
import sys
from os import path

TEST = 't' in sys.argv or '-t' in sys.argv
VERBOSE = 'v' in sys.argv or '-v' in sys.argv
directory = path.dirname(path.abspath(__file__))
path = path.join(directory, 'test') if TEST else path.join(directory, 'input')
with open(path, 'r') as f:
	line = f.readline()

MARKER_LEN = 14

for index, c in enumerate(line):
	if index >= MARKER_LEN:
		if len(set(line[index - MARKER_LEN: index])) == MARKER_LEN:
			if VERBOSE:
				print(set(line[index - MARKER_LEN: index]))
			break

print(f'End of marker index: {index}')

