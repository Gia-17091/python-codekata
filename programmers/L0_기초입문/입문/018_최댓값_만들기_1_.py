# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 22. 00:49:01

def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

#numbers의 원소중 두 수를 곱하시오
#return 이것을 최댓값을 만들어