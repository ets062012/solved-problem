class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        positives = [x for x in nums if x > 0]
        negatives = [x for x in nums if x < 0]
        for i in range(len(positives)):
            result.append(positives[i])
            result.append(negatives[i])
        return result
        