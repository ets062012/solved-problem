class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack (i, path,s):
           
            if s==target:
                ans.append(path[:])
                return
            
            if i>=len(candidates) or s>target:
                return
       
            path.append(candidates[i])
            
           
            backtrack(i,path, s+candidates[i])

            path.pop()
            backtrack(i+1,path,s)

            
        
        ans=[]
        
        backtrack(0,[],0)
       
        return ans
        
        