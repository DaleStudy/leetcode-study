'''
Time Complexity: O(n log n)
- intervals 배열을 정렬하는데 소요되는 시간 (n은 intervals의 길이)
- 배열을 순회하며 겹치는 구간을 찾는데 소요되는 시간 O(n)이나 전체 시간 복잡도에 영향을 주지 않음

# Space Complexity: O(1)
- last_end, count 변수를 사용하는데 필요한 공간
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end = intervals[0][1]
        count = 0

        for val in intervals[1:]:
            if (val[0] < last_end):
                print(val)
                count += 1
            if (val[0] >= last_end):
                last_end = val[1]
        return count
