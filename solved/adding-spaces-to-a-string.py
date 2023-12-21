class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = list(s)
        result = [''] * (len(arr) + len(spaces))

        i, j = 0, 0
        for idx in range(len(result)):
            if j < len(spaces) and idx == spaces[j] + j:
                result[idx] = ' '
                j += 1
            else:
                result[idx] = arr[i]
                i += 1

        return "".join(result)
      
    

            
            
      
            
        
        
        