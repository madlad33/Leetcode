from collections import defaultdict,Counter
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
#         d = defaultdict(list)
#         c = {}
#         for i in range(len(nums)):
#             if nums[i] not in d:
#                 d[nums[i]] = []
#         check = 0   
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 d[nums[i]].append(nums[i]*nums[j])
        
#         for i in d.keys():
#             result = d[i]
#             for j in result:
#                 # print(j)
#                 if j in c:
#                     c[j]+=1
#                 else:
#                     c[j] = 1
#         count = 0   
#         for i in c.keys():
#             if c[i] == 4:
#                 count+=1
#         print(c)
        product = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                mul = nums[i] * nums[j]
                if mul in product:
                    product[mul].append((nums[i],nums[j]))
                else:
                    product[mul] = [(nums[i],nums[j])]
        res = 0
        for i,j in product.items():
            if len(j)>1:
                res+= (len(j)*(len(j)-1))//2*8
                
        return res
        
            
        
            
                
        
                
        
                    
            