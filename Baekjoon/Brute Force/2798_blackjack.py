import itertools
n, max = map(int, input().split())
card = list(map(int, input().split()))

a = list(itertools.permutations(card, 3))

max_ = 0

for i in range (0, len(a)):
    k = sum(a[i])
    if k <= max and k > max_:
        max_ = k

answer = max_

print(answer)
