"""
[문제풀이]
# Inputs
[(0, 8), (8, 10)] -> 튜플 배열

# Outputs
모든 미팅 시간에 대해 참여할 수 있는지에 대한 여부

# Constraints
0 <= intervals 배열 <= 10^4
구간 길이 : 2


# Ideas
정렬 후 각 요소 순회히면서, 첫번째 오른쪽 값보다 두번째 왼쪽 값이 크거나 같으면 통과
아니면 false?

[회고]

"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here

        intervals.sort(key=lambda x: (x[0]))
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True


# 해설
# 제출 코드와 동일!


