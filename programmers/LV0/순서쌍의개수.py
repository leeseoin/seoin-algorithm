def solution(n):
    
    answer = 0
    
    for i in range(1, n+1):
        # print(i)
        for a in range(1, n+1):
            # print(a)
            if i * a == n:
                print(f"i*a={i}*{a}")
                answer+=1
        
    
    return answer