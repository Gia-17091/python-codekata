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

"""
공부 내용
if (a+b) > c 
    and (b+c) > a 
    and (c+a) > b:
    return 1
이것을 Python에서는 "문장 끝"으로 인식한다.
고로, 
#1 괄호로 묶기
if (
    (a+b) > c 
    and (b+c) > a 
    and (c+a) > b
    ):
    return 1
#2 역슬래시 사용
if (a+b) > c \
   and (b+c) > a \
   and (c+a) > b:
    return 1
의 조치가 필요하며, #1이 실무 및 리뷰에서 권장하는 방식이다.
"""
