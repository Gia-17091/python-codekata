# 나누어 떨어지는 숫자 배열
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 알고리즘: 배열, 정렬
# 작성자: 김하은
# 작성일: 2026. 02. 27. 12:19:58

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        return [-1]
    
    return sorted(answer)