# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 23. 09:57:09

def solution(my_string):
    vowels = "aeiou"
    result = ""

    for i in my_string:
        if i not in vowels:
            result += i

    return result
