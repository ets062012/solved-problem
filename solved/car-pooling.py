class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1001 
    
    
        for passengers, start, end in trips:
            timeline[start] += passengers
            timeline[end] -= passengers
    
   
        current_passengers = 0
        for passengers_at_location in timeline:
            current_passengers += passengers_at_location
            if current_passengers > capacity:
                return False
    
        return True

        