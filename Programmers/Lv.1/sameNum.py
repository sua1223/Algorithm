def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if(i!=answer[len(answer)-1]):
            answer.append(i)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))