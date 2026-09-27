class Solution:
    """
    @param m: an integer
    @param n: an integer
    @return: the total number of unlock patterns of the Android lock screen
    """
    def numberOfPatterns(self, m, n):
        def backtrack(curr, visited):
            if len(visited) >= m:
                self.count += 1
            if len(visited) == n:
                return
            for next_ in range(1, 10):
                if next_ in visited:
                    continue
                edge = (min(curr, next_), max(curr, next_))
                if edge not in skip or skip[edge] in visited:
                    visited.add(next_)
                    backtrack(next_, visited)
                    visited.remove(next_)
                    
        skip = {
            (1, 3) : 2,
            (1, 7) : 4,
            (1, 9) : 5,
            (2, 8) : 5,
            (3, 7) : 5,
            (3, 9) : 6,
            (4, 6) : 5,
            (7, 9) : 8
        }
        self.count = 0
        '''
        for curr in range(1, 10):
            backtrack(curr, set([curr])) # curr, visited
        '''
        backtrack(1, set([1]))
        backtrack(2, set([2]))
        self.count *= 4
        backtrack(5, set([5]))
        return self.count