def solution(numbers):
    answer = 0
    
    
    
    max1 = max(numbers)
    print(max1)
    sort = sorted(numbers)[-2]
    print(sort)
    answer=max1*sort
    
    
    return answer