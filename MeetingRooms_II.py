from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Determines the minimum number of meeting rooms required to accommodate all the meetings.
        
        Approach:
        1. Sort all meetings by their start times so we can process them in the order they occur.
        2. Use a min-heap to keep track of the end times of meetings currently using a room.
        3. For each meeting, check if it can reuse an existing room (i.e., if its start time
           is after or equal to the earliest end time). If yes, free up that room.
        4. If a room cannot be reused, allocate a new room by adding the meeting's end time to the heap.
        5. After processing all meetings, the size of the heap will indicate the total number of rooms required.
        """
        
        # Step 1: Sort the meetings by their start time to process them in order
        intervals.sort(key=lambda x: x[0])  # Sort by the start time (x[0])

        # Step 2: Create a min-heap to keep track of meeting end times
        # The heap helps us efficiently track the earliest end time of all active meetings
        min_heap = []  # This will store the end times of meetings

        # Step 3: Process each meeting in the sorted list
        for meeting in intervals:
            start_time, end_time = meeting  # Unpack the meeting's start and end times

            # If the current meeting's start time is >= the earliest end time (heap root),
            # it means the room with the earliest end time is now free.
            if min_heap and min_heap[0] <= start_time:
                heapq.heappop(min_heap)  # Free up the room by removing the earliest end time

            # Step 4: Allocate a room for the current meeting by adding its end time to the heap
            # This either reuses an existing room or allocates a new one
            heapq.heappush(min_heap, end_time)

        # Step 5: The size of the heap indicates the number of rooms required
        # Each end time in the heap represents an active meeting using a room
        return len(min_heap)

# Example usage
solution = Solution()

# Test case 1
meetings1 = [[0, 30], [5, 10], [15, 20]]
print(solution.minMeetingRooms(meetings1))  # Output: 2

# Test case 2
meetings2 = [[7, 10], [2, 4]]
print(solution.minMeetingRooms(meetings2))  # Output: 1
