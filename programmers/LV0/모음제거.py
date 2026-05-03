def solution(my_string):
    answer = ''
    m = ["a","e","i","o","u"]
    
    for i in m:
        my_string = my_string.replace(i, "")
        print(my_string)
        
    return answer