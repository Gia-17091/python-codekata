# 컨트롤 제트
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 03. 28. 02:05:58

def solution(s):
    answer = []
    for i in s.split():
        if i != "Z":
            answer.append(int(i))
        else:
            answer.pop() 
    return sum(answer)