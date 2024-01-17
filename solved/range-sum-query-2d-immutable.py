class NumMatrix:

    def __init__(self, c: List[List[int]]):
        rows,cols=len(c),len(c[0])
        self.arr=[[0]*(cols+1) for i in  range(rows+1)]
        
        for r in range(rows):
            prefix=0
            for coli in range(cols):
                prefix+=c[r][coli]
                above=self.arr[r][coli+1]
             
                self.arr[r+1][coli+1]=prefix+above
        



        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2=row1+1,col1+1,row2+1,col2+1
        br=self.arr[r2][c2]
        above=self.arr[r1-1][c2]
        left=self.arr[r2][c1-1]
        topleft=self.arr[r1-1][c1-1]
        return br-above-left+topleft



        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)