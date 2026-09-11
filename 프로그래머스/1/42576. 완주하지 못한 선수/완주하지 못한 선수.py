def solution(participant, completion):
    # 1. 참가자와 완주자 이름을 각각 정렬
    participant.sort()
    completion.sort()
    
    # 2. 완주자 명단과 순서대로 비교
    for i in range(len(completion)):
        # 이름이 다르면 현재 참가자가 완주하지 못한 사람
        if participant[i] != completion[i]:
            return participant[i]
    
    # 3. 여기까지 전부 같으면,
    #    참가자 명단의 마지막 사람이 완주하지 못한 사람
    return participant[-1]