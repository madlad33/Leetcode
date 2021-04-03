class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        return self.letter_case_permutation(S,'',[])
        
    
    def letter_case_permutation(self,inp,out,arr):
        if len(inp) == 0:
            arr.append(out)
            return

        if inp[0].isalpha():
            i = inp[0]
            out_1  = out
            out_2 = out
            out_1+=i.lower()
            out_2+=i.upper()
            inp = inp[1:]
            self.letter_case_permutation(inp,out_1,arr)
            self.letter_case_permutation(inp,out_2,arr)
        else:
            out_1 = out
            out_1 += str(inp[0])
            inp = inp[1:]
            self.letter_case_permutation(inp,out_1,arr)
        return arr
        