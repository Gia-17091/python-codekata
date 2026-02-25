# 하샤드 수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 알고리즘: 수학, 문자열
# 작성자: 김하은
# 작성일: 2026. 02. 25. 09:04:06

def solution(x):
    list = [int(i) for i in str(x)]
    sum_x = sum(list)
    
    if x % sum_x == 0:
        return True
    else:
        return False