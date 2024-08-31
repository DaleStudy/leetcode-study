from typing import Dict


class Solution:
    # Time: O(n)
    # Space: O(n)
    # ---
    # 1. Prepare a table for caching. Initially put trivial answers for n = 1, 2.
    # Space: O(n)
    cacheTableOfAnswerByN: Dict[int, int] = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        # 2. Use caching.
        # Time: O(1)
        try: return self.cacheTableOfAnswerByN[n]
        except KeyError:
            # 3. Simply, the answers follow Fibonacci sequence. Use recursion.
            # O(n)
            answerBeforeTwoSteps = self.climbStairs(n - 2)
            # 4. Cache the answer during recursion.
            self.cacheTableOfAnswerByN[n - 2] = answerBeforeTwoSteps
            answerBeforeOneStep = self.climbStairs(n - 1)
            self.cacheTableOfAnswerByN[n - 1] = answerBeforeOneStep
            return answerBeforeTwoSteps + answerBeforeOneStep
