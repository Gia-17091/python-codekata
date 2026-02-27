# 음양 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 알고리즘: 배열
# 작성자: 김하은
# 작성일: 2026. 02. 27. 18:21:14

def solution(absolutes, signs):
    return sum(i if sign else -i for i, sign in zip(absolutes,signs))