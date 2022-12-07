

with open('day1/input', 'r') as f:
	lines = f.readlines()

highest_total = 0
current_total = 0
for line in lines:
	if line != '\n':
		current_total += int(line)
	else:
		highest_total = max(current_total, highest_total)
		current_total = 0

print(f'The elf carrying the most calories is carrying {highest_total} calories.')
