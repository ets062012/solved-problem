class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = {}
        for i, restaurant in enumerate(list1):
            if restaurant in list2:
                index_sum[restaurant] = i + list2.index(restaurant)
        min_sum = min(index_sum.values())
        result = [restaurant for restaurant, sum in index_sum.items() if sum == min_sum]
        return result
                
