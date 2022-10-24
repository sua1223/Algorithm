# 프로그래머스 주차 요금 계산

def calc_time(start, end):
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    
    if end_h == start_h:
        total_time = end_m - start_m
    else:
        total_time = (end_h - start_h - 1) * 60 + (60 - start_m) + end_m
    
    return total_time

def calc_fee(time, fees):
    stand_time = fees[0]
    stand_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]
    return_fee = 0
    if time <= stand_time:
        return stand_fee
    else:
        time -= stand_time
        return_fee += stand_fee
        
        if time % per_time == 0:    # 나누어 떨어질 경우
            return_fee += (time // per_time) * per_fee
        else:
            return_fee += ((time // per_time)+1) * per_fee
    
    return return_fee

def solution(fees, records):
    answer = []
    car_dict = {}
    car_time = {}
    car_info = {}
    for r in records:
        time, car_id, info = r.split(' ')
        if car_id not in car_dict and info == "IN":     # 첫 입차
            car_dict[car_id] = time
            car_time[car_id] = 0
            car_info[car_id] = "IN"
        elif car_id in car_dict and info == "OUT":      # 출차 계산
            start = car_dict[car_id]
            end = time
            car_time[car_id] = car_time[car_id] + calc_time(start, end)
            car_info[car_id] = "OUT"
        elif car_id in car_dict and info == "IN":       # n 번째 입차
            car_dict[car_id] = time
            car_info[car_id] = "IN"
    
    
    info_list = list(car_info.values())
    info_id_list = list(car_info.keys())
    
    for i in range(len(info_list)):
        if info_list[i] == "IN":
            tmp_id = info_id_list[i]
            start = car_dict[tmp_id]
            end = "23:59"
            car_time[tmp_id] += calc_time(start, end)
    
    car_time = sorted(car_time.items())
    for k in car_time:
        tmp_id, tmp_time = k
        answer.append(calc_fee(tmp_time, fees))
    
    return answer