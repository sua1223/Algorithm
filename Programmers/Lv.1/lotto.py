def solution(lottos, win_nums):
    answer = []

    for i in lottos:
        if i in win_nums:
            win_nums.remove(i)

    correct = 6 - len(win_nums)

    lowest = 7 - correct
    highest = 7 - correct - lottos.count(0)

    if lowest == 7:
        lowest = 6

    if highest == 7:
        highest = 6

    answer.append(highest)
    answer.append(lowest)

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]	))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))