"""
시간 복잡도: O(N)
공간 복잡도: O(N)
- 새로운 배열을 만들어 리턴하기 떄문이다.

기존 intervals 리스트에 새 interval을 삽입하여 겹치는 구간을 병합하는 코드입니다.
intervals는 이미 정렬되어 있다고 가정하며,
새로운 interval과의 겹침 여부를 판별하여 겹치면 병합하고, 그렇지 않으면 적절한 위치에 삽입합니다.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        added = False

        for start, end in intervals:
            if added:
                ans.append([start, end])
                continue

            if end < newInterval[0]:
                ans.append([start, end])
            elif start > newInterval[1]:
                ans.append(newInterval)
                ans.append([start, end])
                added = True
            else:
                newInterval = [min(start, newInterval[0]), max(newInterval[1], end)]

        if not added:
            ans.append(newInterval)

        return ans
