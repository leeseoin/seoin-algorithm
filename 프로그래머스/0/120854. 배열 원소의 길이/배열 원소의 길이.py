def solution(strlist):
    answer = []
    for i in strlist:
        print(i)
        print(type(i))
        print(len(i))
        answer.append(len(i))
    return answer