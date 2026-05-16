def solution(numbers):
    answer = []
    
    for i in numbers:
        print(f"i:{i}")
        i *= 2
        answer.append(i)
    return answer