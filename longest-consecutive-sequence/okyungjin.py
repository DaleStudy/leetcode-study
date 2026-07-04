from typing import List

# [문제]
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# [요구사항]
# - 정수 배열 nums가 주어진다.
# - nums의 숫자를 사용해서 연속된 숫자를 만들 수 있는 가장 긴 길이를 반환한다.
# - 시간 복잡도가 O(N)인 알고리즘을 작성해야 한다. > 정렬 불가능

# [접근법]
# 문제 요구사항에 O(N)으로 풀게 되어있지만 당장 떠오르는 방식
# 1. 배열을 오름차순으로 정렬한다.
# 2. 정렬된 배열을 순회하며 연속된 숫자일 경우 curLen, maxLen을 갱신하며 가장 긴 길이를 구한다.
# 3. 같은 숫자가 나올 경우 curLen을 유지하며 다음 루프로 넘긴다.
# 4. for문이 종료되면 가장 긴 길이인 maxLen을 반화한다.

# [더 알아볼 것]
# - O(N)으로 푸는 방법 고민해보기


# Time: O(n log n)
# Space: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort() # Time: O(NlogN)

        maxLen = 1
        curLen = 1

        for idx in range(1, len(nums)):
            # 중복 숫자는 길이에 포함하지 않음
            if nums[idx] == nums[idx - 1]:
                continue

            # 이전 숫자 + 1이면 연속
            if nums[idx] == nums[idx - 1] + 1:
                curLen += 1
            else:
                curLen = 1

            maxLen = max(maxLen, curLen)

        return maxLen


# Solution().longestConsecutive([1,100])
# Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])
# Solution().longestConsecutive([])
