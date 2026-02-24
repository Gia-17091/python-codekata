# 한 번만 등장한 문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120896
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 02. 24. 12:24:17

def solution(s):
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    one_times = []
    for ch, count in counts.items():
        if count == 1:
            one_times.append(ch)

    one_times.sort()
    answer = ''.join(one_times)
    return answer