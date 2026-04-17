# 7기 풀이
# 시간 복잡도: O(n^2)
# - 각 원소마다 이전 인덱스들을 모두 확인하므로 이중 for문을 돌아야 함
# 공간 복잡도: O(n)
# - dp 계산을 위한 리스트는 nums의 길이에 의존
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 각 인덱스에서의 최대 길이를 저장하는 dp 리스트
        dp = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            # i 인덱스까지의 최대 길이를 계산 하기 위해
            # 이전 인덱스들 중 가장 긴 길이를 찾아내어 저장하는 장식이다.
            max_lis = 1
            for j in range(0, i):
                # j 인덱스의 의미는 i보다 이전 인덱스 탐방하기 위함
                if nums[j] < nums[i]:  # 이전 인덱스(j 인덱스)에 있는 값이 i 인덱스의 값보다 작다면
                    # 기존의 max_lis와 j 인덱스까지의 최대 길이 값 + 1(i 인덱스 포함한 길이)를 비교하여
                    # 더 큰 수를 max_list에 업데이트 해준다.
                    max_lis = max(max_lis, dp[j] + 1)
            
            # 계산된 max_lis를 dp[i]에 업데이트
            dp[i] = max_lis

        return max(dp)
