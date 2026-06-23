from typing import List

def brightest_position(lights: List[List[int]]) -> int:

    events=[]

    current_brightness=0
    maximun_brightness=float('-inf')
    max_pos=0

    for pos, r in lights:

        start= pos-r
        end= pos+ r

        events.append((start,1))
        events.append((end+1,-1 ))

    events.sort()    


    for pos, delta in events:

        current_brightness+= delta

        if current_brightness> maximun_brightness:
            maximun_brightness= current_brightness
            max_pos=pos

    return max_pos        
