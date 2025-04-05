class Solution:
    def rob(self, nums: List[int]) -> int:
        # 예외 처리: 집이 2개 이하일 경우 그 중 큰 값이 최대 도둑질 금액
        if len(nums) < 3:
            return max(nums)

        # DP(Dynamic Programming)를 위한 메모이제이션 배열
        # memo[0]: 첫 번째 집까지 고려했을 때 최대 도둑질 금액
        # memo[1]: 두 번째 집까지 고려했을 때 최대 도둑질 금액
        memo = [nums[0], max(nums[0], nums[1])]

        # 세 번째 집부터 순차적으로 도둑질 시나리오 검토
        # 매 집마다 두 가지 선택이 있음: 현재 집을 털거나 vs 털지 않거나
        for num in nums[2:]:
            # 현재 집을 털 경우: 현재 집 금액 + 전전 집까지의 최대 금액
            # (인접한 집은 털 수 없으므로 바로 이전 집은 건너뜀)
            robbed = memo[0] + num

            # 현재 집을 털지 않는 경우: 이전 집까지의 최대 금액을 그대로 유지
            not_robbed = memo[1]

            # 메모이제이션 배열 업데이트
            # 다음 반복을 위해 memo[0]은 이전까지의 최대값으로 갱신
            memo[0] = memo[1]
            # memo[1]은 현재까지의 최대값(현재 집을 털거나 안 털거나 중 더 큰 값)으로 갱신
            memo[1] = max(robbed, not_robbed)

        # 마지막 집까지 고려했을 때의 최대 도둑질 금액 반환
        return memo[1]
