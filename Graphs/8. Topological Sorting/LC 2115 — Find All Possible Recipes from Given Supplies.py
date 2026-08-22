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

from typing import List

class Solution:
    def findAllRecipes(
        self,
        recipes: List[str],
        ingredients: List[List[str]],
        supplies: List[str]
    ) -> List[str]:

        available = set(supplies)

        # recipe name -> its ingredients
        recipe_map = {}

        for i in range(len(recipes)):
            recipe_map[recipes[i]] = ingredients[i]

        visiting = set()

        def dfs(recipe):

            # We already know how to obtain this
            if recipe in available:
                return True

            # It's neither a supply nor something we can make
            if recipe not in recipe_map:
                return False

            # Currently checking this recipe already
            # means dependency cycle
            if recipe in visiting:
                return False

            visiting.add(recipe)

            for ingredient in recipe_map[recipe]:

                if not dfs(ingredient):
                    visiting.remove(recipe)
                    return False

            visiting.remove(recipe)

            # We proved that we can make this recipe.
            # It now becomes available just like a supply.
            available.add(recipe)

            return True


        answer = []

        for recipe in recipes:

            if dfs(recipe):
                answer.append(recipe)

        return answer


        





        