def solution(nums):
    # 1. 총 폰켓몬 수의 절반만 가져갈 수 있음
    can_choose = len(nums) // 2
    
    # 2. 중복을 제거하면 폰켓몬 종류만 남음
    kind_count = len(set(nums))
    
    # 3. 종류가 절반보다 많아도, 실제로는 절반 마리만 선택 가능
    #    따라서 둘 중 더 작은 값을 반환
    return min(can_choose, kind_count)