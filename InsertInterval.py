class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        length = len(intervals)
        result = list()
        i = 0
        # Adding all the intervals that ends before new interval starts to the result
        while i < length and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Now the remaining intervals ends after new interval starts, and only if the intervals that starts before new interval ends overlaps with new interval
        # So in this while loop, all the intervals overlaps with the new interval
        while i < length and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        result.append(newInterval)

        # Adding the remaining intervals that starts after new interval ends
        while i < length:
            result.append(intervals[i])
            i += 1
        
        return result
