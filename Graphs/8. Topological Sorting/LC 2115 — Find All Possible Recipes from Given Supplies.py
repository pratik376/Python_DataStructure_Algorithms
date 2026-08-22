from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        q=deque()
        adj= defaultdict(list)
        indegree=defaultdict(int)
        answer=[]
        recipes_set=set(recipes)
        supplies= set(supplies)


        for i in range(len(recipes)):

            for j in ingredients[i]:

                adj[j].append(recipes[i])

                indegree[recipes[i]]+=1


        for recipe in recipes:

            if indegree[recipe]==0:
                q.append(recipe)


        def bfs(q):
            nonlocal answer

            while q:

                recipe=q.popleft()

                if recipe in recipes:
                    answer.append(recipe)

                for ingredient in adj[recipe]:

                    if ingredient in supplies:

                        indegree[ingredient]-=1

                        if indegree[ingredient]==0:
                            q.append(ingredient)
                    else:
                        answer.pop() # if ingrdient is not in supplies we can't make that recipie 
                        break

        bfs(q)

        return answer
        





        