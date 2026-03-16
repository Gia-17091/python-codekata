# 내적
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 알고리즘: 배열, 수학
# 작성자: 김하은
# 작성일: 2026. 03. 16. 16:43:56

def solution(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total