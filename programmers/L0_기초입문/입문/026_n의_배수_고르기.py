# n의 배수 고르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120905
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 22. 11:36:42

def solution(n, numlist):
    result = []
    for i in numlist:
        if i % n ==0:
            result.append(i)
    return result