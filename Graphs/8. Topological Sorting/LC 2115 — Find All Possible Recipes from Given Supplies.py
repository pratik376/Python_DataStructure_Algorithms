from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        q=deque(supplies)
        
        adj= defaultdict(list)
        indegree=defaultdict(int)
        answer=[]
        recipes_set=set(recipes)
    


        for i in range(len(recipes)):

            for j in ingredients[i]:

                adj[j].append(recipes[i])

                indegree[recipes[i]]+=1

    
        def bfs(q):
            nonlocal answer

            while q:

                ingredient=q.popleft()

                if ingredient in recipes_set:
                    answer.append(ingredient)

                for nei in adj[ingredient]:
                    indegree[nei]-=1

                    if indegree[nei]==0:
                        q.append(nei)
                

        bfs(q)

        return answer
        





        