class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_arr=[]
        n=len(intervals)
        for i in range(len(intervals)):
            sorted_arr.append([intervals[i],i])
        sorted_arr.sort()
        
        def binary_search(val):
            low=0
            high=len(intervals)-1
            if sorted_arr[n-1][0][0]<val:
                return -1
           
            while low<=high:
                mid=(low+high)//2
                if sorted_arr[mid][0][0]>=val:
                    high=mid-1
                else:
                    low=mid+1
            return sorted_arr[low][1]
        result=[-1]*len(intervals)
        for i in range(len(intervals)):
            result[i]=binary_search(intervals[i][1])
        return result
            
                

        