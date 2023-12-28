class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        good_integers = set()
        not_good_integers = set()
    
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                not_good_integers.add(fronts[i])
            else:
                good_integers.add(fronts[i])
                good_integers.add(backs[i])
    
        min_good_integer = float('inf')
        for num in good_integers:
            if num not in not_good_integers:
                min_good_integer = min(min_good_integer, num)
    
        return min_good_integer if min_good_integer != float('inf') else 0
        