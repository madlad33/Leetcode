class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = target
        # b = target - a
        d = {}
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in d:
                return [i,d[nums[i]]]
            else:
                d[diff] = i
        
                
            