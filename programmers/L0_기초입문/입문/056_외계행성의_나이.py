# 외계행성의 나이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 02. 06. 02:18:02

def solution(age):
    answer = ''
    char = ['a','b','c','d','e','f','g','h','i','j']

    for i in str(age):
        answer += char[int(i)]  

    return answer
