def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
                continue
            if j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
                continue

            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[len(triangle)-1])