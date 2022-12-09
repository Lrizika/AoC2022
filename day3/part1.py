
import sys

DAY = 3
TEST = 'test' in sys.argv
path = f'day{DAY}/test' if TEST else f'day{DAY}/input'
with open(path, 'r') as f:
	lines = f.readlines()


priority_map = {}
for i in range(26):
	priority_map[chr(i + ord('a'))] = i + 1
	priority_map[chr(i + ord('A'))] = i + 27


def get_shared_items(sack: str) -> list:
	shared_items = []
	compartment1 = sack[:len(sack) // 2]
	compartment2 = sack[len(sack) // 2:]
	for item in compartment1:
		if item in compartment2:
			shared_items.append(item)
	return shared_items


tot_priority = 0
for line in lines:
	shared_items = set(get_shared_items(line.rstrip('\n')))
	tot_priority += sum(
		[priority_map[item] for item in shared_items]
	)

print(f'Total priority: {tot_priority}')

