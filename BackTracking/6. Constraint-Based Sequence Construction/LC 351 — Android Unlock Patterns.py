class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        count=0
        used= [False] * len(tiles)

        tiles= "".join(sorted(tiles))
        
        def dfs(path):
            nonlocal count

            if len(path) > len(tiles):
                return
            
            if len(path)>0:
                count+=1

            for i in range(len(tiles)):

                if i> 0 and tiles[i]== tiles[i-1] and not used[i-1]:
                    continue

                if used[i]:
                    continue

                used[i]=True
                path.append(tiles[i])

                dfs(path)

                path.pop()
                used[i]=False   
        dfs([])
        return count
            












        