class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Intuition:
            이전까지의 누적합에서 현재 원소를 추가할지 말지에 대한
            결정을 매 iteration마다 반복한다.
            현재 원소를 추가했을 경우(누적합 + 현재 원소)와
            현재 원소를 시작으로 하는 경우(현재 원소)를 비교하여
            dp 배열을 갱신한다.

        Time Complexity:
            O(N):
                리스트를 1번 순회하며 답을 찾으므로,
                O(N)의 시간복잡도가 소요된다.

        Space Complexity:
            O(N):
                dp 배열에 N개의 time step을 저장하므로
                O(N)의 공간복잡도가 소요된다.

        Key takeaway:
            초기에는 two pointer 방식을 생각했으나
            해결을 하지 못해서 답안을 확인했다.
            O(N)의 시간복잡도를 가지는 경우, DP도 풀이가
            될 수 있음을 인지하자.
        """
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            cumsum = dp[i - 1] + nums[i]
            cur = nums[i]
            if cumsum > cur:
                dp[i] = cumsum
            else:
                dp[i] = cur

        return max(dp)
