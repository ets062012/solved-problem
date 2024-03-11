class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        high=len(matrix)-1
       
        while low<=high:
            mid=(low+high)//2
            if target>matrix[mid][-1]:
                low=mid+1
            elif target<matrix[mid][0]:
                high=mid-1
            else:
               break
        if not (low<=high):
            return False
        mid=(low+high)//2
        l=0
        h=len(matrix[0])-1

        while l<=h:
            m=(l+h)//2
            if matrix[mid][m]>target:
                h=m-1
            elif matrix[mid][m]<target:
                l=m+1
            else:
                return True
        return False
        


        
