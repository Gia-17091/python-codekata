# 나머지가 1이 되는 수 찾기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 알고리즘: 수학, 반복문
# 작성자: 김하은
# 작성일: 2026. 01. 21. 17:00:43

def solution(n):
    for x in range(2,n):
        if n%x==1:
            return x