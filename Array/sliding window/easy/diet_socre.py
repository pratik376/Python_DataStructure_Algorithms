from typing import List

def calculate_score(sum,score, lower, upper):
    if sum < lower:
        score-=1
    elif sum>upper:
        score+=1  

    return score    

def dietPlanPerformance(calories: List[int], k: int, lower: int, upper: int) -> int:

    score=0
    sum=0
    i=0

    sum= sum(calories[:k])
    # for l in range(k):
    #     sum+=calories[l]

    score= calculate_score(sum,score,lower,upper)    

    for j in range(k, len(calories)):

        sum+= calories[j]- calories[i]
        score= calculate_score(sum,score,lower,upper) 

        i+=1    

    return score          




# count += 1 if len(set(s[i:i+3])) == 3 else 0