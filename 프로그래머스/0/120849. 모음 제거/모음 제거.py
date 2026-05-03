def solution(my_string):
    answer = my_string
    m = ["a","e","i","o","u"]
    
    for i in m:
        answer = answer.replace(i, "")
        print(answer)
        
        
    return answer

# def solution(my_string):
#     vowels = ['a','e','i','o','u']
#     for vowel in vowels:
#         my_string = my_string.replace(vowel, '')
#     return my_string