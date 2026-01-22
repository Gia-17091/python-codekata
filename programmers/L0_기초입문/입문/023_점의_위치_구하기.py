# 점의 위치 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841
# 알고리즘: 기초
# 작성자: 김하은
# 작성일: 2026. 01. 22. 10:54:37

def solution(dot):
    x, y = dot
    if dot[0]>0 and dot[1] >0:
        return 1
    elif dot[0]<0 and dot[1] >0:
        return 2
    elif dot[0]<0 and dot[1] <0:
        return 3
    else:
        return 4
'''
x,y 대입을 생각하지 못했던 문제..
if x > 0:
    return 1
처럼 정의되지 않아 에러가 생길것을 우려.
(NameError: name 'x' is not defined)

하지만, 
x, y = dot 는 대입문(assign statement; 변수를 새로 만드는 문장)을 사용하면 가능함을 알게되었음.
'''