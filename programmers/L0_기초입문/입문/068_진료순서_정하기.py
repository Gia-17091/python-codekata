# 진료순서 정하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 03. 26. 10:44:50

def solution(emergency):
    answer = []
    for i in emergency:
        count = 0
        for j in emergency:
            if j > i:
                count += 1
        answer.append(count + 1)
    return answer