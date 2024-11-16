from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        - Idea: i번째 집까지의 최대 금액은 두 가지 중 더 큰 값으로 결정된다.
            1. (i-2번째 집까지의 최대 금액) + i번째 집의 금액
            2. (i-1번째 집까지의 최대 금액)
            이를 이용해 동적 프로그래밍으로 각 집까지의 최대 금액을 계산한다.

            다만, 맨 마지막 집과 첫번째 집이 이어진 사이클(cycle) 형태이기 때문에
            첫번째 집과 마지막 집이 동시에 도둑맞을 수는 없다.
            이를 처리하기 위해 두 가지 경우로 나눠서 각각 계산하고, 둘 중 더 큰 값을 선택한다.
            1. 첫번째 집을 포함하고 마지막 집을 포함하지 않는 경우
            2. 첫번째 집을 포함하지 않고 마지막 집을 포함하는 경우
        - Time Complexity: O(n). n은 집의 개수.
            모든 집을 한번씩 순회해야 하므로 O(n) 시간이 걸린다.
        - Space Complexity: O(n). n은 집의 개수.
            각 집까지의 최대 금액을 저장하기 위해 배열을 사용하므로 O(n) 만큼의 메모리가 필요하다.
        """
        if len(nums) == 1:
            return nums[0]

        dp1 = [0] + [0] * len(nums)
        dp1[1] = nums[0]

        dp2 = [0] + [0] * len(nums)
        dp2[1] = 0

        for i in range(2, len(nums) + 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i - 1])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i - 1])

        return max(dp1[-2], dp2[-1])
