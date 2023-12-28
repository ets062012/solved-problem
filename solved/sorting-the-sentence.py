class Solution:
    def sortSentence(self, s: str) -> str:
        s=list(s.split(" ")) 
        track={int(s[i][len(elem)-1:]):s[i][:len(elem)-1] for i,elem in enumerate(s)} 
         
        new=dict(sorted(track.items(),key=lambda x:x[0])) 
        
        ans=[] 
        ans+=new.values() 
        
        return " ".join(ans)
        