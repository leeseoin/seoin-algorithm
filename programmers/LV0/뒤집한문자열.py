def solution(my_string):
    
    reversed_string = ""
    answer = ""
    for i in my_string:
        print(f"i:{i}")
        
        answer = reversed_string + i
        """
        1. "" = ""+j -> answer=j
        2. "j" = "" +a -> 
        """
        print(f"answer:{answer}")
    
    return answer