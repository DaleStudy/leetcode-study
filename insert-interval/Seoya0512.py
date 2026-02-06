'''
Time Complexity : O(N)
- newInterval을 삽입할 위치 탐색 O(N)
- Intervals 병합을 위해 for문으로 모든 구간을 순회 O(N)
- O(N) + O(N) = O(N)

Space Complexity : O(N)
- output 리스트에 모든 구간을 저장 O(N)

'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        while idx < len(intervals) and intervals[idx][0] < newInterval[0]:
            idx +=1
        intervals.insert(idx, newInterval)    # newInterval을 삽입할 위치 탐색 (O(N))

        # Intervals 병합
        output = [intervals[0]]
        for interval in intervals[1:]:
            # 이전 구간과 겹치는 경우
            if output[-1][1] >= interval[0]:
                output[-1][1] = max(output[-1][1], interval[1])
            else:
                output.append(interval)
        return output
        