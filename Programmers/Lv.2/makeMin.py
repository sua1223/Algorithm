# star time 05:06 / end time 05:10
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(0, len(A)):
        answer += A[i] * B[i]

    return answer


print(solution([1,4,2],[5,4,4]))