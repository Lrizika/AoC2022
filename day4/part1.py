
import sys

DAY = 4
TEST = 'test' in sys.argv
path = f'day{DAY}/test' if TEST else f'day{DAY}/input'
with open(path, 'r') as f:
	lines = f.readlines()


def get_section_overlap(s1: range, s2: range) -> range:
	left_bound = max(min(s1), min(s2))
	right_bound = min(max(s1), max(s2))
	return range(left_bound, right_bound + 1)


def get_range(range_str: str) -> range:
	rmin, rmax = range_str.split("-")
	# print(f'{range_str}: {range(int(rmin), int(rmax) + 1)}')
	return range(int(rmin), int(rmax) + 1)


complete_overlap_count = 0
for line in lines:
	s1_str, s2_str = line.rstrip('\n').split(',')
	s1, s2 = get_range(s1_str), get_range(s2_str)
	overlap = get_section_overlap(s1, s2)
	if overlap == s1 or overlap == s2:
		complete_overlap_count += 1

print(f'Complete overlap count: {complete_overlap_count}')

