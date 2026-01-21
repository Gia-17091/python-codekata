# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 22. 00:56:57

def solution(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if (a+b) > c and (b+c)>a and (c+a)>b:
        return 1
    else:
        return 2