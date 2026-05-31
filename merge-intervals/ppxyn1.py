# idea : -
# TimeComplexity: # O(n log(n))
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals) 
        output = [intervals[0]]

        # Merge when intervals overlap
        for start, end in intervals[1:]:
            lastEnd = output[-1][1] 
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


