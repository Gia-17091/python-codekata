# 중복된 문자 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 02. 12. 09:31:17

def solution(my_string):
    answer=[]
    for char in my_string:
        if char not in answer:
            answer.append(char)
    
    return''.join(answer)