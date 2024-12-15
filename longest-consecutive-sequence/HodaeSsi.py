from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.child = None

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        dict = {}

        for num in nums:
            if dict.get(num) is None:
                dict[num] = Node(num)
                if dict.get(num + 1) is not None:
                    dict[num + 1].child = dict[num]
                    dict[num].parent = dict[num + 1]
                
                if dict.get(num - 1) is not None:
                    dict[num].child = dict[num - 1]
                    dict[num - 1].parent = dict[num]
                
        for key in dict.keys():
            if dict[key].parent is None:
                node = dict[key]
                count = 1

                while node.child is not None:
                    count += 1
                    node = node.child

                answer = max(answer, count)

        return answer

