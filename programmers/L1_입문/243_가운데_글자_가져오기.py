# 가운데 글자 가져오기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 알고리즘: 문자열
# 작성자: 김하은
# 작성일: 2026. 01. 21. 01:04:33

def solution(s):
    if len(s)%2==0:
       return s[len(s)//2 -1 : len(s)//2+1]
    else:
        return s[len(s)//2]