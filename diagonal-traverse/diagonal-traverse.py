class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        d = (m + n) - 1 
        diag = [[] for i in range(d)]
        
        for i in range(m):
            for j in range(n):
                s = i+j
                diag[s].append(mat[i][j])
                
        for i in range(len(diag)):
            for j in range(len(diag[i])):
                if i % 2 == 0:
                    l = diag[i][::-1]
                    result.append(l[j])
                else:
                    result.append(diag[i][j])
        
        return result
                
    