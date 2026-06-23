class FreqStack:
    
    def __init__(self):
        self.cnt={}
        self.maxCnt=0
        self.stacks={}

    def push(self, val : int) -> None:

        valCnt= 1+ self.cnt.get(val,0)
        self.cnt[val]=valCnt

        if valCnt > self.maxCnt:
            self.maxCnt=valCnt
            self.stacks[self.maxCnt]=[]

        self.stacks[valCnt].append(val)


    def pop(self) ->int:

        res= self.stacks[self.maxCnt].pop()
        self.cnt[res]-=1

        if not self.stacks[self.maxCnt]:
            self.maxCnt-=1

        return res                


import collections

class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.freq = collections.defaultdict(int)
        self.groups = collections.defaultdict(list)

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f

        self.max_freq = max(self.max_freq, f)

        self.groups[f].append(val)

    def pop(self) -> int:
        val = self.groups[self.max_freq].pop()

        self.freq[val] -= 1

        if not self.groups[self.max_freq]:
            self.max_freq -= 1

        return val
