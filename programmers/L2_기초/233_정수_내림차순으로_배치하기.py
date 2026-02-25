# 정수 내림차순으로 배치하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 알고리즘: 문자열, 정렬
# 작성자: 김하은
# 작성일: 2026. 02. 25. 09:02:18

def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    return int(''.join(answer))