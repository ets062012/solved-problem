class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        r=len(p)
        arr=list(s)
        dict1=Counter(p)
        dict2=Counter(s[:len(p)])
        ans=[]
        
        while r<len(arr):
            # if sum(dict2)==len(p):
            if dict1==dict2:
                ans.append(l)
            dict2[arr[l]]-=1
                
                
            dict2[arr[r]]+=1
            
                
            l+=1
            r+=1
        print(dict2)
        if dict1==dict2:
            ans.append(l)

        return ans  


                

            

                
            
            


        