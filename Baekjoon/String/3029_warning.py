from datetime import datetime

present_time = input()
throw_time = input()

present_h = int(present_time.split(':')[0])
present_m = int(present_time.split(':')[1])
present_s = int(present_time.split(':')[2])

throw_h = int(throw_time.split(':')[0])
throw_m = int(throw_time.split(':')[1])
throw_s = int(throw_time.split(':')[2])

a = datetime(2000, 1, 1, present_h, present_m, present_s)
b = datetime(2000, 1, 1, throw_h, throw_m, throw_s)
c = str(b - a)

answer = c[-8:]

if answer[0] == ' ':
    answer = '0'+answer[1:]

if answer[1] == ':':
    answer = '0'+answer

if answer == "00:00:00":
    answer = "24:00:00"

print(answer)