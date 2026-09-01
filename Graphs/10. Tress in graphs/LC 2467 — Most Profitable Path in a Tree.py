from typing import List

from collections import defaultdict, deque
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        adj= defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        bob_times={}

        def dfs(src,prev,time):

            if src==0:
                bob_times[src]=time
                return True

            for nei in adj[src]:

                if nei!= prev:
                   if dfs(nei,src,time+1):
                       bob_times[src]=time
                       return True

            return False

        dfs(bob,-1,0)

        q=deque([0,0,-1,amount[0]]) # (node, time, parent, total profit)

        res=float("-inf")

        while q:
           node, time, parent, profit =q.popleft()

           for nei in adj[node]:

               if nei == parent:
                   continue

               nei_profit= amount[nei]
               nei_time= time+1

               if nei in bob_times:
                   
                 if nei_time > bob_times[nei]:
                     nei_profit=0

                 if nei_time == bob_times:
                     nei_profit = nei_profit//2

               q.append((nei,nei_time,node, nei_profit+profit))

               if len(adj[nei])==1:
                   res= max(res,nei_profit+profit)
        return res
                   
                   


            

        



      
            






        