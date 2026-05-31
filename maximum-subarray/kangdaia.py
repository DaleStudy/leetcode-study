class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """리스트의 이어진 문자열로 구성된 subarray중 최대 합을 찾는 함수

        방법:
        1. brute force. 다만 O(n)으로 만들 수 없어 탈락!
        2. 전역 최대합과 로컬 최대 합을 분리해서 생각하기.
            연속된 문자열이기 때문에, 현재 값이 이전의 합보다 크면 앞의 값을 버리는 방식
            => 시간 복잡도 O(n), 공간 복잡도 O(1)
        3. divide and conquer (Follow up)

        Args:
            nums (list[int]): 정수 문자열

        Returns:
            int: 최대 합
        """
        max_sum = nums[0]
        local_sum = nums[0]
        for i in range(1, len(nums)):
            if local_sum < 0 and local_sum < nums[i]:
                local_sum = nums[i]
            else:
                local_sum += nums[i]
            max_sum = max(max_sum, local_sum)
        return max_sum

    def maxSubArraySubtle(self, nums: list[int]) -> int:
        def divConq(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            mid = (left + right) // 2

            left_max = divConq(left, mid)
            right_max = divConq(mid + 1, right)

            curr_sum = 0
            left_suffix_max = -float("inf")
            for idx in range(mid, left - 1, -1):
                curr_sum += nums[idx]
                left_suffix_max = max(left_suffix_max, curr_sum)

            curr_sum = 0
            right_prefix_max = -float("inf")
            for idx in range(mid + 1, right + 1, 1):
                curr_sum += nums[idx]
                right_prefix_max = max(right_prefix_max, curr_sum)

            cross = left_suffix_max + right_prefix_max
            return max(left_max, right_max, cross)

        return divConq(0, len(nums) - 1)
