# 프로그래머스 뉴스 클러스터링

def solution(str1, str2):
    answer = 0
    
    str1_list = []
    str2_list = []
    for i in range(len(str1)):
        str1_list.append(str1[i].upper())
    
    for i in range(len(str2)):
        str2_list.append(str2[i].upper())
    
    tmp = ''
    set_1 = []
    set_2 = []
    for i in range(len(str1_list) - 1):
        tmp = str1_list[i] + str1_list[i+1]
        print(tmp)
        if tmp.isalpha():
            set_1.append(tmp)
    
    for i in range(len(str2_list) - 1):
        tmp = str2_list[i] + str2_list[i+1]
        if tmp.isalpha():
            set_2.append(tmp)
    
    # 공집합, 공집합인 경우
    if len(set_1) == 0 and len(set_2) == 0:
        return 1 * 65536
    
    # 교집합 만들기
    set1_visit = []
    set2_visit = []
    for i in range(len(set_1)):
        set1_visit.append(0)
    for i in range(len(set_2)):
        set2_visit.append(0)
    
    inter_set = []
    for i in range(len(set_1)):
        for j in range(len(set_2)):
            if set_1[i] == set_2[j] and set1_visit[i] == 0 and set2_visit[j] == 0:
                inter_set.append(set_1[i])
                set1_visit[i] = 1
                set2_visit[j] = 1
    
    inter = len(inter_set)
    
    # 합집합 만들기
    union_set = inter_set
    for i in range(len(set_1)):
        if set1_visit[i] == 0:
            union_set.append(set_1[i])
    for i in range(len(set_2)):
        if set2_visit[i] == 0:
            union_set.append(set_2[i])
    uni = len(union_set)
        
    answer = inter / uni
    return int(answer * 65536)