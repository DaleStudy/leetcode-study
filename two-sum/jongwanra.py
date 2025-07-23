"""
[Problem]
https://leetcode.com/problems/two-sum/description/

nums.length <= 10^4  => 10,000 * 10,000 => n^2 time complexity일 경우 1초 이상 소요

[Plan]
nums를 hash table로 만들자. (key: element, value: index)
이후에 nums를 돌면서 target - current_num을 뺀 값이 hash table에 존재한 경우 return하자.
그랬을 경우, O(n) 시간 복잡도를 예상한다.

[Complexity]
N: nums length
Time: O(N) => HashTable에 nums를 만큼 반복문 돌림
Space: O(N) => nums length 만큼 반복문을 돌면서  hash table을 생성
"""

class Solution(object):
    def twoSum(self, nums, target):
        num_to_index_map = dict()
        for index in range(len(nums)):
            num_to_index_map[nums[index]] = index

        for index in range(len(nums)):
            num = nums[index]
            diff = target - num
            # target - num 값이 존재 하지 않을 경우 무시
            if not diff in num_to_index_map:
                continue
            # index가 자기 자신인 경우 무시
            if index == num_to_index_map[diff]:
                continue
            return [index, num_to_index_map[diff]]

        return [0, 0]


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))

