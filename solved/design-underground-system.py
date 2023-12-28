class UndergroundSystem:
    def __init__(self):
        self.check_ins = {}  # {id: (start_station, start_time)}
        self.trips = {}  # {(start_station, end_station): (total_time, total_count)}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins[id]
        end_station = stationName
        total_time = t - start_time
        if (start_station, end_station) in self.trips:
            prev_total_time, prev_total_count = self.trips[(start_station, end_station)]
            self.trips[(start_station, end_station)] = (prev_total_time + total_time, prev_total_count + 1)
        else:
            self.trips[(start_station, end_station)] = (total_time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_count = self.trips.get((startStation, endStation), (0, 0))
        if total_count == 0:
            return 0
        return total_time / total_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)