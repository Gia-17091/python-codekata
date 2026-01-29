# 옷가게 할인 받기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 30. 02:24:54

def solution(price):
    answer = 0
    if price >=100000 and price<300000:
        return int(price*0.95)
    elif price >=300000 and price <500000:
        return int(price*0.90)
    elif price>=500000:
        return int(price*0.8)
    else:
        return price