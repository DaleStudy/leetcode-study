from typing import List
from typing import Set
from typing import Tuple


class Solution:
    target: int
    candidates: List[int]
    answers: Set[Tuple[int]]

    # Time: O(k^N)
    # Space: O(N^2)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.candidates = candidates
        self.answers = set()
        self.findAnswers(0, [])
        return list(self.answers)

    def findAnswers(self, currentSum: int, nums: List[int]):
        assert currentSum < self.target, "Given sum should be smaller than the target."
        for num in self.candidates:
            if currentSum + num < self.target:
                # 1. Continue finding.
                # Time: O(k^N)
                # Space: O(N^2). Max total size of all "nums" = 1 + 2 + ... + N.
                self.findAnswers(currentSum + num, nums + [num])
            if currentSum + num > self.target:
                # 2. Stop finding.
                continue
            if currentSum + num == self.target:
                # 3. Add the answer.
                self.answers.add(tuple(sorted(list(nums + [num]))))
        return
