class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        _sum  = 0 
        count = 0
        min_len = float('inf')
            
        while j<len(nums):            
            _sum+=nums[j]
            
            if _sum >= target:
                min_len = min(min_len,j-i+1)
                while _sum > target:
                    _sum -= nums[i]
                    i+=1
                    if _sum >=target:
                        min_len = min(min_len,j-i+1)
                j+=1   
                
            elif _sum < target:
                j+=1
        
        if min_len == float('inf'):
            return 0
        return min_len
            
                
