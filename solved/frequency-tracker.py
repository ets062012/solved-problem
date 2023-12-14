class FrequencyTracker:

    def __init__(self):
        self.dict = {}
        self.freq = {}

    def add(self, number: int) -> None:
        prev_freq = self.dict.get(number, 0)
        self.dict[number] = prev_freq + 1
        if prev_freq in self.freq:
            self.freq[prev_freq] -= 1
            if self.freq[prev_freq] == 0:
                del self.freq[prev_freq]
        if prev_freq + 1 in self.freq:
            self.freq[prev_freq + 1] += 1
        else:
            self.freq[prev_freq + 1] = 1

    def deleteOne(self, number: int) -> None:
        if number in self.dict and self.dict[number] > 0:
            prev_freq = self.dict[number]
            self.dict[number] = prev_freq - 1
            if prev_freq in self.freq:
                self.freq[prev_freq] -= 1
                if self.freq[prev_freq] == 0:
                    del self.freq[prev_freq]
            if prev_freq - 1 > 0:
                if prev_freq - 1 in self.freq:
                    self.freq[prev_freq - 1] += 1
                else:
                    self.freq[prev_freq - 1] = 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq


        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)