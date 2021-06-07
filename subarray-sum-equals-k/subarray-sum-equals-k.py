class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d =  {}
        count = 0
        d[0] = 1
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            count += d.get(s-k,0)
            d[s] = d.get(s,0) + 1
        return count
