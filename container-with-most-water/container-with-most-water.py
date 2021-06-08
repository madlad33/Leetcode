class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1
        max_area = float('-inf')
        while i <= j:
            min_ele = min(height[i],height[j])
            area = min_ele * abs(i-j)
            if min_ele == height[i]:
                i += 1
            else:
                j -= 1
            max_area = max(max_area,area)
        return max_area