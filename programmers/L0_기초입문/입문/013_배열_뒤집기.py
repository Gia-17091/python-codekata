# 배열 뒤집기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120821
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 20. 10:19:05

# 처음 생각한 풀이
def solution(num_list):
    return num_list[::-1]

# 다른 방식을 찾아본 풀이
def solution(num_list):
    num_list.reverse()
    return num_list
