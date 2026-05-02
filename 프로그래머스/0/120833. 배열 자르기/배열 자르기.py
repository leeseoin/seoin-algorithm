def solution(numbers, num1, num2):

    answer = []

    for i in range(num1, num2+1):
        print(i)
        answer.append(numbers[i])
        print(answer)
        
    
    return answer