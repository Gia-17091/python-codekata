# 자연수 뒤집어 배열로 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 알고리즘: 문자열, 배열
# 작성자: 김하은
# 작성일: 2026. 02. 24. 13:00:14

def solution(n):
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer