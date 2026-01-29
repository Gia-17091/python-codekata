# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 29. 13:00:41

def solution(array):
    array.sort()
    n = len(array)
    mid = n//2    #몫을 구하는 연산자 // 사용
    if n%2==0:
        return (array[mid-1]+array[mid+1])/2
    else:
        return array[mid]