# 기존에 풀었던거
def solution(n):
    answer = 0
    for i in n+1:
        print(i)
        if i % 2 == 0:
            print(f"짝수:{i}")
            answer+=i
            print(answer)
    return answer
solution(10)
print(solution)

# iterable 에러가 떠서 고쳐서 바꾼것
def solution2(n):
    answer = 0
    for i in range(0, n+1):
        print(i)
        if i % 2 == 0:
            print(f"짝수:{i}")
            answer+=i
            print(answer)
    return answer
solution2(10)
print(solution2)