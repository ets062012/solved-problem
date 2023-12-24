class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
       
        c=0
        for col in zip(*strs):
           
           
            if sorted(col)!=list(col):
                
                c+=1
        return c


        
        


          

        