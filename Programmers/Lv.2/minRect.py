# start time 11:36      end time 11:40
def solution(sizes):
	for card in sizes:
		card.sort()

	max_len, max_height = 0, 0
	for card in sizes:
		if card[0] > max_len:
			max_len = card[0]
		if card[1] > max_height:
			max_height = card[1]

	return max_len * max_height

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))