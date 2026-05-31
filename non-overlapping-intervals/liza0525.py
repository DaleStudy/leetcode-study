# 7기 풀이
# 시간 복잡도: O(n log n)
# - sorting에 O(n log n), 이후 전체 탐색에 O(n)
# - 종합 O(n log n)
# 공간 복잡도: O(1)
# - 추가 자료구조 없이 변수만 사용
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # end 기준으로 구간들을 오름차순
        res = 0

        prev_end = intervals[0][1]  # 제일 첫번째 구간의 end를 prev_end로 저장

        for curr_start, curr_end in intervals[1:]:  # 1번 인덱스부터 loop
            if  curr_start < prev_end:  # 이전 구간 end와 curr_start 구간이 겹칠 때
                res += 1  # res를 하나 올린다
            else:  # 겹치지 않는다면
                prev_end = curr_end  # 지금 구간의 end를 다음 loop의 prev_end가 되도록 할당

        return res
