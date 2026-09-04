def solution(array, commands):
    answer = []

    # commands의 [i, j, k]를 하나씩 처리
    for i, j, k in commands:
        # 파이썬 인덱스는 0부터 시작하므로 i는 -1 처리
        # j는 슬라이싱에서 끝 인덱스를 포함하지 않지만, j번째까지 포함하려면 그대로 사용하면 됨
        sliced = array[i - 1:j]

        # 잘라낸 배열 정렬
        sliced.sort()

        # k번째 값 추가
        # 파이썬은 0번째부터 시작하므로 k - 1
        answer.append(sliced[k - 1])

    return answer