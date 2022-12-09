
from ast import parse
import sys

DAY = 5
TEST = 'test' in sys.argv
path = f'day{DAY}/test' if TEST else f'day{DAY}/input'
with open(path, 'r') as f:
	lines = f.readlines()


def parse_stacks(lines):
	for box_footer_index, line in enumerate(lines):
		if line[:2] == ' 1':
			box_count = int(line.rstrip(' \n').split(' ')[-1])
			break
	stacks = {v: [] for v in range(1, box_count + 1)}
	for line in reversed(lines[:box_footer_index]):
		for box in range(1, box_count + 1):
			box_index = box * 4 - 3
			if box_index < len(line) and line[box_index] != ' ':
				stacks[box].append(line[box_index])
	return stacks, box_footer_index, box_count


def do_move(stacks, move):
	count = int(move.lstrip('move ').split(' ')[0])
	move_details = move.lstrip(' move1234567890')
	origin = int(move_details.lstrip(' from').split(' ')[0])
	destination = int(move_details.split(' ')[-1])
	moving = stacks[origin][-count:]
	stacks[origin] = stacks[origin][:-count]
	stacks[destination] = stacks[destination] + moving


stacks, box_footer_index, box_count = parse_stacks(lines)
for line in lines[box_footer_index + 1:]:
	if line == '\n':
		continue
	if TEST:
		print(stacks)
		print(line)
	do_move(stacks, line.rstrip('\n'))

top_of_stacks = [stacks[box][-1] for box in range(1, box_count + 1)]

print(f'Uppermost boxen: {"".join(top_of_stacks)}')



