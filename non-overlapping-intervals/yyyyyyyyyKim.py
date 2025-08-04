class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # 그리디
        # 시간복잡도 O(n log n), 공간복잡도 O(1)
        
        # 시작점 기준 정렬
        intervals.sort()
        answer = 0  # 제거할 개수
        curr_end = intervals[0][1]  # 첫 구간 끝나는 지점 초기화

        for i in range(1,len(intervals)):
            start, end = intervals[i]

            # 겹치는 경우(제거)
            if start < curr_end:
                # 현재 구간 제거
                answer += 1
                # 더 작은 지점 남기기(겹치는 부분을 줄이기위해)
                curr_end = min(curr_end, end)
            
            # 안겹치는 경우(현재 구간을 다음 기준으로 탐색)
            else:
                curr_end = end
                
        return answer
