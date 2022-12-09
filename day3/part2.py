
import sys

DAY = 3
TEST = 'test' in sys.argv
path = f'day{DAY}/test' if TEST else f'day{DAY}/input'

priority_map = {}
for i in range(26):
	priority_map[chr(i + ord('a'))] = i + 1
	priority_map[chr(i + ord('A'))] = i + 27


def get_badge(sacks: list) -> str:
	for item in sacks[0]:
		for sack in sacks[1:]:
			if item not in sack:
				break
		else:
			return item
	return sentinel


tot_priority = 0
with open(path, 'r') as f:
	while True:
		sacks = [f.readline().rstrip('\n') for i in range(3)]
		if sacks == ['', '', '']:
			break
		tot_priority += priority_map[get_badge(sacks)]

print(f'Total priority: {tot_priority}')

