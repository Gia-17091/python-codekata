# 369게임
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120891
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 02. 07. 14:19:02

def solution(order):
    answer = 0
    for i in str(order):
        if int(i) % 3 == 0 and int(i) != 0:
            answer += 1
    return answer
