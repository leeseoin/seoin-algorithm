def solution(number):
    answer = 0
    n = len(number)

    # 서로 다른 학생 3명을 뽑기 위해
    # i < j < k 순서로 모든 조합을 확인
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # 세 학생의 번호 합이 0이면 삼총사
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer