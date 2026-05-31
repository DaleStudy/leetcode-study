# 7기 풀이
# 시간 복잡도: O(n)
# - intervals의 모든 요소를 접근하므로 intervals의 길이(n)만큼 시간 소요
# 공간 복잡도: O(1)
# - 결과 변수인 res를 제외하면, 몇 가지 변수 이외에 사용하지 않음
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [newInterval]  # newInterval을 맨 처음에 넣어줌

        for curr_start, curr_end in intervals:  # intervals를 돌며 현재의 구간을 curr_start, curr_end로 지정
            prev_start, prev_end = res[-1]  # 이전 구간은 res의 마지막 요소인 prev_start, prev_end로 지정
            if curr_start <= prev_end:
                # 1. curr_start가 prev_end와 작거나 같다는 것은
                # 다음의 두 케이스로 나뉘어진다.(자세한 설명은 각 조건 내에 상술)
                if curr_end < prev_start:
                    # 1-1. curr 구간이 prev 구간보다 아예 앞서는 경우
                    # 이 경우에는 구간의 순서를 변경해줘야 하므로
                    # res[-1]을 curr 요소로 변경해준 후
                    # prev 구간을 다시 append해준다.
                    res[-1][0], res[-1][1] = curr_start, curr_end
                    res.append([prev_start, prev_end])
                else:
                    # 1-2. curr 구간과 prev 구간이 겹치는 경우
                    # 이 경우에는 start끼리 비교하여 작은 수를 res[-1]의 start로
                    # end 끼리 비교하여 큰 수를 res[-1]의 end 값으로 재할당
                    res[-1][0] = min(curr_start, prev_start)
                    res[-1][1] = max(curr_end, prev_end)
            else:
                # 2. curr_start가 prev_end보다 큰 경우에는
                # 구간의 순서를 바꾸거나 겹치는 구간을 merge할 필요가 없으므로
                # res에 현재 구간을 append해준다.
                res.append([curr_start, curr_end])

        return res
