def solution(phone_number):
        answer=phone_number[len(phone_number)-4:]
        answer='*'*(len(phone_number)-4)+answer
        return answer

print(solution("01033334444"))
print(solution("027778888"))