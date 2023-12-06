class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lexical={}
        for i,val in enumerate(order):
           
            lexical[val]=i
        for s1 in range(len(words)-1):
            curr_word1=words[s1]
            curr_word2=words[s1+1]
            n=min(len(curr_word1),len(curr_word2))
            
           
            
        
            for i in range(n):
                if lexical[curr_word1[i]] == lexical[curr_word2[i]]:
                    continue
                elif lexical[curr_word1[i]] > lexical[curr_word2[i]]:
                    return False
                else:
                    break
            if curr_word1[:n]==curr_word2[:n] and len(curr_word1)>len(curr_word2):
                return False

        return True






        