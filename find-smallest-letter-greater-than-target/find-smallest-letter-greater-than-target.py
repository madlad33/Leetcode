class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ascii_val = list(map(ord,letters))
        target_ord = ord(target)
        min_val = float('inf')
        for i in ascii_val:
            if i > target_ord:
                min_val = min(min_val,i)
        
        if min_val == float('inf'):
            return str(chr(ascii_val[0]))
                
        return str(chr(min_val))

            
            
        