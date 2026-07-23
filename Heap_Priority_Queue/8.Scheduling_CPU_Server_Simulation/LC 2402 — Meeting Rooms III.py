from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        avalible_rooms= [(i,0) for i in range(len(n))]  # (room_number, metting_number)
        busy_rooms=[] # ( free_time, room_number, metting_number)

        meetings.sort(key=lambda x: x[0]) # or simply meetings.sort() they both are the same

        for i in range(len(meetings)):

            start_time, end_time= meetings[i]


            while busy_rooms and start_time >= busy_rooms[0][0]:
               freeTime, room_num, meeting_number =heapq.heappop(busy_rooms)
               heapq.heappush(avalible_rooms,meeting_number)

            if not avalible_rooms:
                freeTime, room_num, meeting_number =heapq.heappop(busy_rooms)

                end_time= freeTime + (end_time-start_time)
                heapq.heappush(busy_rooms, (end_time, room_num,meeting_number+1))
         
            room_num, meeting_number=heapq.heappop(avalible_rooms)

            heapq.heappush(busy_rooms, (end_time,room_num, meeting_number+1))


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        available_rooms = [i for i in range(n)]
        busy_rooms=[] # (end_time, room_number)
        count=[0] *n
        meetings.sort()

        for start, end in meetings:

            while busy_rooms and start >= busy_rooms[0][0]:
                _, room_no= heapq.heappop(busy_rooms)

                heapq.heappush(available_rooms,room_no)

            if not available_rooms:
                 _, room_no= heapq.heappop(busy_rooms)










       

        
        
                
        