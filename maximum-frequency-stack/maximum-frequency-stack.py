from collections import Counter, defaultdict
class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = collections.defaultdict(list) 
        self.maxfreq = 0
        

    def push(self, val: int) -> None:
        #increment the frequency by 1 
        f = self.freq.get(val,0) + 1
        self.freq[val] = f
        if f > self.maxfreq: 
            self.maxfreq = f
        self.group[f].append(val) 

        
    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if len(self.group[self.maxfreq]) == 0 :
            self.maxfreq -= 1

        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()