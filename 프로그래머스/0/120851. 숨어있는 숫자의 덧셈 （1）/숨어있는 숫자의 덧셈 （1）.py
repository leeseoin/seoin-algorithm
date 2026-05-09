def solution(my_string):
    answer = 0
    for a in my_string:
        print(f"a:{a}")
        print(type(a))
        # a.isdigit()
        print(f"a.isdigit():{a.isdigit()}")
        if a.isdigit() == True:
            answer+=int(a)
            print(f"answer:{answer}")
    return answer