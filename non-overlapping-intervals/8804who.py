class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        answer, end = 0, -inf
        intervals.sort(key = lambda x:x[1])

        for i_s, i_e in intervals:
            if end <= i_s:
                end = i_e
            else:
                answer += 1
            
        return answer
    
