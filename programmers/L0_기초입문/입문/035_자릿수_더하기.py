# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 23. 17:10:19

def solution(n):
    total = 0
    for i in str(n):  #int는 반복 불가능. str()로 바꾸기
        total += int(i)
    return total
