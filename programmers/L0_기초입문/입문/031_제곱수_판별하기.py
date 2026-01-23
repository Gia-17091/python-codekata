# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 23. 09:36:35

def solution(n):
    for i in range(1,n+1):
        if i ** 2 ==n:
            return 1
    return 2
'''
else가 없는 이유!

else가 if문 바로 아래에 있다면, 이번 i가 아니다 = 전체가 아님.
하지만, 반복이 끝난 뒤에 없으면 return 2를 해!라는 코드를 작성이 목표이므로, for문 밖에 return을 작성.

def solution(n):
    for i in range(1, n+1):
        if i ** 2 == n:
            return 1
    else:
        return 2
의 경우는 for의 else로, for문이 중간에 break/return 없이 끝났을 때만 실행하자!는 의미를 같기에, 이 코드로 작성해도 무방하다:)

'''
