from collections import defaultdict,Counter
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
#         product = {}
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 mul = nums[i] * nums[j]
#                 if mul in product:
#                     product[mul].append((nums[i],nums[j]))
#                 else:
#                     product[mul] = [(nums[i],nums[j])]
#         res = 0
#         for i,j in product.items():
#             if len(j)>1:
#                 res+= (len(j)*(len(j)-1))//2*8
                
#         return res
    
    product = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                mul = nums[i] * nums[j]
                if mul in product:
                    product[mul]+=1
                else:
                    product[mul] = 1
        res = 0
        for i,j in product.items():
            if j>1:
                res+= ((j)*((j)-1))//2*8
                
        return res
        
            
        
            
                
        
                
        
                    
            
