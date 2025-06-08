# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            nums를 순회하며 현재 보고 있는 값 num이 포함되는 max subarray product를 구하기 위해서는
            max(이전 값과 연속되는 subarray인 경우, 이전 값과 연속되지 않는 subarray인 경우)를 구해야 한다.
                - num이 양수일 때: max(이전까지의 max subarray product * num, num)
                - num이 음수일 때: max(이전까지의 min subarray product * num, num)
            따라서 매 단계마다 이전까지의 max subarray product(= max_p)와 min subarray product(= min_p)를 트래킹해야 한다.
        """
        res = max_p = min_p = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # 1. num이 음수라면, max_p와 min_p 바꿔치기
            # if num < 0:
            #     max_p, min_p = min_p, max_p

            # 2. max_p, min_p 업데이트
            # max_p = max(max_p * num, num)
            # min_p = min(min_p * num, num)

            # 1 & 2번 대신, 다중 할당으로 처리 가능
            max_p, min_p = max(max_p * num, min_p * num, num), min(max_p * num, min_p * num, num)

            # 3. res 값 업데이트
            res = max(res, max_p)

        return res
