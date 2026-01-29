# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 30. 02:46:18

def solution(hp):
    # 장군개미(공격력 5)
    general_ant = hp // 5
    remaining = hp % 5

    # 병정개미(공격력 3)
    soldier_ant = remaining // 3
    remaining = remaining % 3

    # 일개미(공격력 1)
    worker_ant = remaining

    # 최소 개미 수 합
    return general_ant + soldier_ant + worker_ant
