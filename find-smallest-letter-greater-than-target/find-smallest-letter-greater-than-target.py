class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ascii_val = list(map(ord,letters))
        target_ord = ord(target)
        min_val = float('inf')
        start  = 0
        end =  len(ascii_val) - 1
        result = 0
        while start <= end:
            mid = (start + end) // 2
            if ascii_val[mid] == target_ord + 1:
                
                return str(chr(ascii_val[mid]))
            elif ascii_val[mid] <= target_ord:
                start = mid + 1
            else:
                result = mid
                end = mid - 1
                
                
        return str(chr(ascii_val[result]))
            

            
            
        