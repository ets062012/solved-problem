class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        arr=[[0]*len(image[0]) for _ in range(len(image))]
        for i in range(len(image)):
            arr[i]=list(reversed(image[i]))
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j]==0:
                    arr[i][j]=1
                elif arr[i][j]==1:
                    arr[i][j]=0
        return arr

        