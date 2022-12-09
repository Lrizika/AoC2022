
import sys
TEST = 'test' in sys.argv
from enum import IntEnum


class RPSChoice(IntEnum):
	A = 1  # Rock
	B = 2  # Paper
	C = 3  # Scissors
	X = 1  # Rock
	Y = 2  # Paper
	Z = 3  # Scissors


def get_score(op_play: str, your_play: str) -> int:
	score = RPSChoice[your_play]
	if RPSChoice[your_play] == RPSChoice[op_play] + 1 or (your_play == 'X' and op_play == 'C'):
		score += 6
	elif RPSChoice[your_play] == RPSChoice[op_play]:
		score += 3
	if TEST:
		print(f'{op_play} {your_play} {score}')
	return score


path = 'day2/test' if TEST else 'day2/input'
with open(path, 'r') as f:
	lines = f.readlines()

tot_score = 0
for line in lines:
	tot_score += get_score(*line.rstrip('\n').split(" "))

print(f'Total score: {tot_score}')

