# 7기 풀이
# 시간 복잡도: O(n log n)
# - merge하는 로직은 intervals의 길이(n)만큼의 시간 소요
# - intervals를 sorting하는 로직은 n log n 만큼의 시간 소요
# 공간 복잡도: O(1)
# - 결과 리스트(res) 제외, 몇 개의 변수만 사용
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 먼저 intervals를 오름차순으로 sorting한다.
        # 각 요소의 첫번째 값을 기준으로 
        intervals.sort()

        i, j = 0, 1
        res = []

        # intervals를 탐색하는 i가 그 길이보다 작을 때 loop를 돈다
        while i < len(intervals):
            curr_start, curr_end = intervals[i]  # 첫번째 머지 대상을 기준으로
            while j < len(intervals):  # j번째 요소들을 계속 머지함(범위 머지가 가능한 한)
                next_start, next_end = intervals[j]
                if curr_start <= next_start <= curr_end:  # 다음 요소의 첫번째 값이 현재 요소 범위 내에 있을 때
                    curr_end = max(curr_end, next_end)  # 더 큰 범위로 머지
                else:  # 그렇지 않으면 이번 텀에서의 머지가 완료된 것이므로 loop 탈출
                    break
                j += 1  # 머지가 가능한 한 j를 계속 올려준다.

            res.append([curr_start, curr_end])  # 머지 완료된 구간은 res에 담고
            i = j  # 이번 loop에서 사용했던 j가 다음 루프의 i가 되고
            j = i + 1  # j는 i의 다음 인덱스부터 다시 머지를 할 수 있도록 변경

        return res
