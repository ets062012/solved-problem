class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        ansf=-1
        ansl=-1
        ans=[]
        while low<=high:
            mid=(high+low)//2
            if nums[mid]==target:
                ansf=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1

            else:
                low=mid+1
        ans.append(ansf)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(high+low)//2
            if nums[mid]==target:
                ansl=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1

            else:
                low=mid+1
        ans.append(ansl)
        return ans
        