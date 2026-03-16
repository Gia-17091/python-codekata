# 약수의 개수와 덧셈
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 알고리즘: 수학
# 작성자: 김하은
# 작성일: 2026. 03. 16. 17:00:47

def solution(left, right):
    answer=0
    for i in range (left, right+1):
        if int(i**0.5)==i**0.5:
            answer-=i
        else:
            answer+=i
    return answer