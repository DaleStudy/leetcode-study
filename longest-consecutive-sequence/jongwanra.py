"""
[Problem]
https://leetcode.com/problems/longest-consecutive-sequence/description/

[Brain Storming]
O(N)으로 연속된 길이를 찾아야 한다?
계수 정렬을 이용하면 가능하다. 하지만 nums[i] <= 10^9이기 떄문에 공간을 너무 많이 잡아먹는다.

[Plan]
1. max num과  min num을 찾는다.
2. set을 통해 O(1)로 빠르게 num을 찾을 수 있도록 변경한다.
3. for loop를 min num ~ max num으로 순회한다
    3-1. 연속된 길이를 비교하며 기록한다.

-> Time Limit Exceeded 발생
-> [0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]

[Plan2]
Heap 자료구조를 이용해서 구한다.
nums를 전부 heapify할 경우 O(N),
nums를 순회하면서 heappop을 할 경우 N * log(N)
"""

import heapq


class Solution(object):
    """
    [Complexity]
    N: nums.length
    M: max_num - min_num + 1
    ---
    Time: O(N + M)
    Space: O(N)

    nums가 [1, 9999999] 일 경우 굉장히 비효율적인 풀이.
    """

    def longestConsecutive1(self, nums):
        if not nums:
            return 0

        min_num = min(nums)
        max_num = max(nums)
        num_set = set(nums)

        answer = 0

        cur_num = min_num
        while cur_num <= max_num:
            count = 0
            while cur_num in num_set:
                count += 1
                cur_num += 1
            answer = max(answer, count)
            cur_num += 1

        return answer

    """
    [Complexity] 
    N: nums.length
    Time: O(N * log N)
    Space: O(N)
    """

    def longestConsecutive2(self, nums):
        if not nums:
            return 0
        heapq.heapify(nums)

        answer = 1
        prev_num = heapq.heappop(nums)
        count = 1

        while nums:
            cur_num = heapq.heappop(nums)
            if cur_num == prev_num:
                continue
            if cur_num - prev_num == 1:
                # 연속인 경우
                count += 1
                prev_num = cur_num
            # 연속이 아닌 경우
            else:
                count = 1
                prev_num = cur_num
            answer = max(answer, count)

        return answer

    """
    다른 사람의 풀이
    참고: https://www.algodale.com/problems/longest-consecutive-sequence/

    [Plan]
    1. nums를 Set에 저장한다.
    2. 모든 정수에 대해서 for-loop를 순회한다.
        2-1. 정수에서 1을 뺀 값이 Set에 있다면, 구간내 첫 번째 값이 될 수 없기 때문에 무시
        2-2. 없다면, 1씩 길이를 최대길이로 늘려본다.
        2-3. 구간내 첫 번째 값이 중복으로 들어갈 수 있는 경우를 대비하여 cache 추가
    3. 최대 구간의 길이와 비교한다.

    [Complexity]
    N: nums.length
    Time: O(N)
    Space: O(N)
    """

    def longestConsecutive(self, nums):
        answer = 0
        num_set = set(nums)
        cache = set()

        for num in nums:
            if num - 1 in num_set:
                continue
            if num in cache:
                continue

            cache.add(num)
            length = 1
            while num + length in num_set:
                length += 1

            answer = max(answer, length)
        return answer


solution = Solution()
# Normal Case
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
print(solution.longestConsecutive([1, 0, 1, 2]) == 3)

# Edge Case
print(solution.longestConsecutive([]) == 0)
print(solution.longestConsecutive([0, 1, 2, 4, 8, 5, 6, 7, 9, 3, 55, 88, 77, 99, 999999999]) == 10)
print(solution.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7)

