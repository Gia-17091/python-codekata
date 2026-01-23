# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 23. 11:19:02

def solution(num_list):
    even =0
    odd =0
    for i in num_list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return [even,odd]