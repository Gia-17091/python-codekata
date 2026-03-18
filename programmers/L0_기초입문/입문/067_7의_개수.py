# 7의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120912
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 03. 18. 14:31:45

def solution(array):
    answer = 0
    for i in array:
        answer += str(i).count('7')
    return answer