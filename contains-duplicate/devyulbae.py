"""
Blind75 - 3. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Counter를 사용한 풀이
Counter 생성에 n번, 조회에 n번 -> O(n)
"""
from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for count in counter.values():
            if count > 1:
                return True
            
        return False