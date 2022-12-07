

with open('day1/input', 'r') as f:
	lines = f.readlines()

highest_three = [0, 0, 0]
current_total = 0
for line in lines:
	if line != '\n':
		current_total += int(line)
	else:
		highest_three = sorted(
			highest_three[:2] + [
				max(highest_three[2], current_total)
			],
			reverse=True
		)
		current_total = 0

print(f'The three elves carrying the most calories are carrying {sum(highest_three)} calories.')
