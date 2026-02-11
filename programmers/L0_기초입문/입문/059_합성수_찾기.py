# 합성수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 02. 11. 17:50:20

def solution(n):
    answer = 0
    for i in range(4,n+1):
        list =[]
        for k in range(1,i+1):
            if i%k==0:
                list.append(k)
        if len(list)>=3:
            answer+=1
    return answer