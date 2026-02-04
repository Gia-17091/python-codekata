# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 02. 05. 04:39:28

def solution(num, k):
    num_str = str(num)
    k_str = str(k)
    if k_str in num_str:
        return num_str.index(k_str)+1
    else:
        return -1