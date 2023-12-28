class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]: 
        dict={}
        arr=[]
        comp=[]
        c=0
        for i in range(len(arr2)):
            if arr2[i] in arr1:
                c= arr1.count(arr2[i])
                dict[arr2[i]]=c
        for i in  range(len(arr1)):
            if arr1[i] not in dict:
                comp.append(arr1[i])
        comp.sort()
       


        for key,val in dict.items():
            arr.extend([key]*val)
        for i in range(len(comp)):
            arr.append(comp[i])
       
       
        return arr

    

            
        