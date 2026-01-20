# 직사각형 별찍기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12969
# 알고리즘: 반복문
# 작성자: 김하은
# 작성일: 2026. 01. 21. 01:14:39

m, n = map(int, input().split())
for i in range(n):
    print('*'*m)