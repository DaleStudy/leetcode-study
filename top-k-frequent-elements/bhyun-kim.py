"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/

Solution:
    - Count the frequency of each element in the list
    - Sort the dictionary by the frequency in descending order
    - Return the first k elements in the sorted dictionary

Time complexity: O(nlogn)
    - Counting the frequency of each element: O(n)
    - Sorting the dictionary: O(nlogn)
    - Returning the first k elements: O(k)
        k <= n
    - Total: O(nlogn)

Space complexity: O(n)
    - Storing the frequency of each element: O(n)
    - Storing the sorted dictionary: O(n)
    - Storing the output: O(k)
        k <= n
"""
from collections import OrderedDict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_dict = OrderedDict()

        for n in nums:
            if n in n_dict:
                n_dict[n] += 1
            else:
                n_dict[n] = 1

        n_dict = sorted(n_dict.items(), key=lambda x: x[1], reverse=True)

        output = [0] * k
        for i in range(k):
            output[i] = n_dict[i][0]

        return output
