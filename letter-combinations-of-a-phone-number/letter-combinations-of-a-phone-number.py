class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        sample_arr = ['']
        if len(digits)==0:
            return []
        def get_keypad(inp):
            if len(inp) == 0:
                return sample_arr
            inp_0 = inp[0]
            rest_inp = inp[1:]
            result = get_keypad(rest_inp)
            code = arr[int(inp_0)]
            new_arr = []
            for i in range(len(code)):
                ch = code[i]
                for j in range(len(result)):
                    new_arr.append(ch+result[j])

            return new_arr
        
        return get_keypad(digits)
        
        