"""
# Constraints

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

# Time Complexity: O(n)

배열 내 원소를 순회하며 각 원소별로 등장횟수를 기록
-> 무슨 원소가 들어있는지 모르므로, defaultdict가 좋아보임
-> 등장 횟수 값이 2 이상인 경우 배열 순회 멈추기

# Space Complexity: O(n)

최대 배열 원소 개수만큼 key-value 지니는 사전 활용
"""

from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict = defaultdict(int)

        for n in nums:
            if count_dict[n] + 1 >= 2 :
                return True

            else :
                count_dict[n] += 1

        return False