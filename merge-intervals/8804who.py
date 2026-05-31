class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        start = intervals[0][0]
        end = intervals[0][1]
        answer = []
        for interval in intervals[1:]+[[10001, 0]]:
            if end < interval[0]:
                answer.append([start, end])
                start = interval[0]
            if interval[1] > end:
                end = interval[1]
        return answer
    
