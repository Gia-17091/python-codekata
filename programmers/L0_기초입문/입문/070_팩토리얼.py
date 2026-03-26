# 팩토리얼
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 03. 27. 08:03:16

def solution(n):
    i=1
    nums=1
    while nums <=n:
        i+=1
        nums *=i
    return i-1