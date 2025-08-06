class Solution:
    """
    부분합 활용
    dp[0] = nums[0]
    dp[1] = dp[0] + nums[1] 와 nums[1] 중 큰 값을 넣는다.
    [-2, 1]까지의 합과 [1]까지의 합 중 큰 값을 넣는다고 생각하면 된다.
    dp[1] = [1]
    dp[2] = dp[1] + nums[2] 와 nums[2] 중 큰 값을 넣는다.
    dp[1]에서 [-2, 1]를 선택했다면 [-2, 1, -3]까지의 합과 [1]을 선택했다면 [1, -3]까지의 합 중 큰 값을 선택하게 된다.
    dp[2] = [1, -3]
    dp[3] = dp[2] + nums[3] 와 nums[3] 중 큰 값을 넣는다.
    dp[3]은 [1, -3]에 [4]를 추가하여 [1, -3, 4]까지의 합과 nums[3]인 4를 비교하여 큰 값으로 넣는다.
    결국 점화식은 dp[i] = max(dp[i-1] + nums[i], nums[i])가 된다.
    
    시간 복잡도 (Time Complexity):
      - dp 배열을 채우기 위해 한 번 순회: O(n)
      - dp 배열에서 최댓값을 찾기 위해 한 번 순회: O(n)
      → 총 시간 복잡도: O(n)

    공간 복잡도 (Space Complexity):
        - dp 배열이 입력 크기만큼 필요: O(n)
        → 총 공간 복잡도: O(n)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
