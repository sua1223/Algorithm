n = int(input())
answer = 0
while True:
    if n % 5 == 0:
        n -= 5
        answer = answer + 1
    elif n - 3 >= 0:
        n -= 3
        answer = answer + 1
    else:
        answer = -1

    if n == 0 or answer == -1:
        break

print(answer)