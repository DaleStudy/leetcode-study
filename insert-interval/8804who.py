class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = 1e9
        new_end = -1

        answer = []

        for start, end in intervals:
            if start <= newInterval[0] <= end or newInterval[0] <= start <= newInterval[1] or newInterval[0] <= end <= newInterval[1] or start <= newInterval[1] <= end:
                if new_start == 1e9:
                    new_start = start
                new_end = end
            else:
                answer.append([start, end])
        new_start = min(new_start, newInterval[0])
        new_end = max(new_end, newInterval[1])
        
        answer.append([new_start, new_end])
        return sorted(answer)
    
