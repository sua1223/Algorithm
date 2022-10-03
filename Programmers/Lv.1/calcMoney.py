# start time 05:18 / end time 05:24

def solution(price, money, count):
    total = 0
    price_ = price
    for i in range(0, count):
        total += price_
        price_ += price

    if total < money:
        return 0

    return total - money


print(solution(3, 20, 4))