class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half) -> List[int]:
            # write your code here
            l=0
            r=0
            n=len(left_half)
            m=len(right_half)
            res=[]
            while l<n  and r<m:
                if left_half[l]<right_half[r]:
                    res.append(left_half[l])
                    l+=1
                else:
                    res.append(right_half[r])
                    r+=1
            res.extend(left_half[l:])
            res.extend(right_half[r:])
            return res
            
            
    

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
        
            return merge(left_half, right_half)
        left=0
        right=len(nums)-1
        return mergeSort(left,right,nums)
