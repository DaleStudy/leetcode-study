from typing import List
from unittest import TestCase, main


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.solveWithDict(nums)

    """
    Runtime: 486 ms (Beats 40.61%)
    Time Complexity:
        - nums 배열 조회하며 연산에 O(n)
        - 크기가 n인 node_dict.items()을 조회, visited에 의해 각 노드당 한 번만 방문,
            - visited가 set이므로 갱신 및 확인에 O(1)
            - 2개 항에 대해 max 연산하므로 O(2)로, 총 O(n)
        > O(n) + O(n) ~= O(n)

    Memory: 44.62 MB (Beats 5.00%)
    Space Complexity: O(n)
        - value가 크기 2짜리 배열이고 key가 최대 n인 dict 변수 사용에 O(2n)
        - 최대 크기가 n인 visited 사용에 O(n)
        > O(2n) + O(n) ~= O(n)
    """
    def solveWithDict(self, nums: List[int]) -> int:
        node_dict = {}
        for num in nums:
            curr_node = [num, num]
            if num - 1 in node_dict:
                prev_node = node_dict[num - 1]
                curr_node[0] = prev_node[0]
                prev_node[1] = curr_node[1]
            if num + 1 in node_dict:
                post_node = node_dict[num + 1]
                curr_node[1] = post_node[1]
                post_node[0] = curr_node[0]
            node_dict[num] = curr_node

        max_length = 0
        visited = set()
        for key, (prev_key, post_key) in node_dict.items():
            while prev_key not in visited and prev_key in node_dict:
                visited.add(prev_key)
                prev_key = node_dict[prev_key][0]
            while post_key not in visited and post_key in node_dict:
                visited.add(post_key)
                post_key = node_dict[post_key][1]
            curr_length = post_key - prev_key + 1
            max_length = max(max_length, curr_length)

        return max_length


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        output = 4
        self.assertEqual(Solution.longestConsecutive(Solution(), nums), output)

    def test_2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        output = 9
        self.assertEqual(Solution.longestConsecutive(Solution(), nums), output)


if __name__ == '__main__':
    main()
