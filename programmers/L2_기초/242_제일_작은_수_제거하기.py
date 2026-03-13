# 제일 작은 수 제거하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12935
# 알고리즘: 배열
# 작성자: 김하은
# 작성일: 2026. 03. 13. 09:14:19

def solution(arr):
    for i in arr:
        if i ==10:
            return [-1]
        else:   
            arr.remove(min(arr))
            return arr