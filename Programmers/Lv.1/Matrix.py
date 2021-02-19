def solution(arr1, arr2):
    answer = []
    tmp=[]
    for i in range(0,len(arr1)):
        for j in range (0,len(arr1[0])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)
        tmp=[]
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
print(solution([[1],[2]],[[3],[4]]))