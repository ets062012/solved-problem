class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
      
        l=0
        r=k
        newstr=blocks[:k]
        
        eval=k
        
        while r<=len(blocks):

            eval=min(eval,newstr.count('W'))
          
            l+=1
            r+=1
            newstr=blocks[l:r]
           
        return eval
       
    
        