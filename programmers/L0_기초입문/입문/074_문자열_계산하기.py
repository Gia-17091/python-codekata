# 문자열 계산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120902
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 04. 06. 17:55:18

def solution(my_string):
    parts = my_string.split()
    result = int(parts[0])
    
    for i in range(1, len(parts), 2):
        if parts[i] == "+":
            result += int(parts[i+1])
        else:
            result -= int(parts[i+1])
    return result