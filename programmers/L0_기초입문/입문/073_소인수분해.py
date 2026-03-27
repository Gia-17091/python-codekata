# 소인수분해
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120852
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 03. 28. 02:18:29

def solution(n):
    answer = []
    for i in range(2,n+1):
        if n%i==0:
            answer.append(i)
            while n%i==0:
                n=n//i
    return answer