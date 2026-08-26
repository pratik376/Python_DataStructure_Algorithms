from typing import List

class Solution:
    def areSentencesSimilarTwo( self,sentence1: List[str],sentence2: List[str],similarPairs: List[List[str]]) -> bool:


        if len(sentence1) != len(sentence2):
            return False

        parents={}
        rank={}

        for pair in similarPairs:

            for p in pair:
                parents[p] = p
                rank[p]=1

        def find(n):

            p= parents[n]

            while p !=parents[p]:
                parents[p]=parents[parents[p]]
                p=parents[p]
            return p

        def union(a1,a2):
            p1,p2= find(a1),find(a2)

            if p1==p2:
                return True

            if rank[p1]> rank[p2]:

                parents[p2]=parents[p1]
                rank[p1]+=rank[p2]

            else:
                parents[p1]=parents[p2]
                rank[p2]+= rank[p1]

         

        for a,b in similarPairs:
            union(a,b)

        for a1,a2 in zip(sentence1,sentence2):



            if find(a1) !=find(a2):
                return False

        return True
            
