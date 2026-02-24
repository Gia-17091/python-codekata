# 숨어있는 숫자의 덧셈 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120864
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 02. 24. 12:51:22

def solution(my_string):
    result = ""
    for i in my_string:
        if i.isdigit():
            result += i
        else:
            result += " "
    
    num = result.split()
    
    total = 0
    for n in num:
        total +=int(n)
    
    return total