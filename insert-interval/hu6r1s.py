class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        output = [intervals[0]]
        for x, y in intervals[1:]:
            if output[-1][1] >= x:
                output[-1][1] = max(y, output[-1][1])
            else:
                output.append([x, y])
        return output


"""
newInterval을 집어넣은 다음 정렬을 해주면 인덱스 0에 있는 값 기준으로 정렬됨
대소 비교를 해서 이전 배열의 인덱스 1이 현재 배열의 인덱스 0보다 크거나 같으면
값을 변경해주고 아니라면 값을 그냥 추가한다.
"""
