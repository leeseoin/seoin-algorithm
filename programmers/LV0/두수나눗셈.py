

def solution(num1, num2):
    answer = (num1 / num2) * 1000
    # format_answer = round(answer, 0)
    format_answer2 = f"{answer:.0f}"
    print(type(format_answer2))
    
    # print(solution(7,2))
    return format_answer2
print(solution(7,2))
# print(type(format_answer))
