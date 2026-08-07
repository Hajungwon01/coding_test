def solution(nums):
    unique_types = len(set(nums))
    
    can_take = len(nums) // 2
    
    return min(unique_types, can_take)