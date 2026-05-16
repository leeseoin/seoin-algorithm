def solution(array):
    answer = 0
    a = array.sort()
    print(a)
    array.sort()
    print(array)
    print(min(array))
    len_a = len(array) // 2
    print(len_a)
    answer = array[len_a]
    
    
    return answer
    # return array