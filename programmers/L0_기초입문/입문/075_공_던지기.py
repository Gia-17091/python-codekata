# 공 던지기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120843
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 04. 06. 18:02:36

def solution(numbers, k):
    answer = (k-1)*2 %len(numbers)
    return numbers[answer]