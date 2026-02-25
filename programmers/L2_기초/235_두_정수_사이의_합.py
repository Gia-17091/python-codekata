# 두 정수 사이의 합
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 알고리즘: 수학
# 작성자: 김하은
# 작성일: 2026. 02. 26. 01:39:23

def solution(a, b):
    num1 = min(a,b)
    num2 = max(a,b)
    
    answer=0
    for i in range(num1,num2+1):
        answer+=i
    return answer