def solution(num_list):
    
    reverse_num_list = num_list[::-1]
    reverse_num_list2 = num_list.reverse()
    print(reverse_num_list2)
    reverse_num_list3 = list(reversed(num_list))

    print(f"슬라이싱:{reverse_num_list}")
    print(f"그냥reverse:{reverse_num_list2}")
    print(f"reversed방식:{reverse_num_list3}")
    
    return reverse_num_list2

print(solution([1,2,3,4,5]))


def solution2(num_list):
    num_list.reverse()
    return num_list
print(solution2([1,2,3,4,5]))
