class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        stack=[]
        for c in nums2:
            while stack and c>stack[-1]:
                a=stack.pop()
                idx=nums1.index(a)
                res[idx]=c
            if c in nums1:
                stack.append(c)
        return res
        