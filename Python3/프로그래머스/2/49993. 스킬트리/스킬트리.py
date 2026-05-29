def solution(skill, skill_trees):
    answer = 0
    
    tmp_list = list(skill)
    

    filter_list = []
    
    for skill_tree in skill_trees:
        tmp_s = ''
        for s in skill_tree:
            if s in tmp_list:
                tmp_s += s
        filter_list.append(tmp_s)
                
    
    print(filter_list)
    for f in filter_list:
        if skill.startswith(f):
            answer += 1
        
    return answer