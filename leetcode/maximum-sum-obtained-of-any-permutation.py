class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n=len(nums)
        total=0

        pre=[0]*(n+1)
        for req in requests:
            pre[req[0]]+=1
            pre[req[1]+1]-=1
        for i in range(1,n):
            pre[i]+=pre[i-1]
        nums.sort(reverse=True)
        pre.sort(reverse=True)
        
        for i in range(n):
            total+=nums[i]*pre[i]
        return total%MOD



        