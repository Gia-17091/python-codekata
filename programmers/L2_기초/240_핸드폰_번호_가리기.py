# 핸드폰 번호 가리기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 알고리즘: 문자열
# 작성자: 김하은
# 작성일: 2026. 03. 12. 20:37:11

def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]