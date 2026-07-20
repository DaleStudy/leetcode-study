"""
Top-down dynamic programming with memoization.

Time Complexity: O(k * n * (n + m)), or O(k * n^2) when m <= n
    - n = len(s)
    - k = len(wordDict)
    - m = the maximum word length

    There are at most n memoized states, and each state checks every word.
    In this implementation, s[index:] also creates a suffix whose length is
    O(n), while startswith may compare up to m characters.

Space Complexity: O(n)
    The memoization table and recursion stack each contain at most n entries.

dp(index) returns whether the suffix beginning at index can be completely
segmented. Reaching len(s) means that all characters have been consumed.
For every dictionary word that matches the current suffix, the function
recursively checks the remaining suffix and stops at the first valid split.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache()
        def dp(index: int) -> bool:
            if index == len(s):
                return True

            for word in wordDict:
                if len(s) - index < len(word):
                    continue

                if s[index:].startswith(word) and dp(index + len(word)):
                    return True

            return False

        return dp(0)

"""
Bottom-up dynamic programming over prefixes of s.

Time Complexity: O(k * n * (n + m)), or O(k * n^2) when m <= n
    - n = len(s)
    - k = len(wordDict)
    - m = the maximum word length

    Each of the n + 1 prefix boundaries checks every word. The expression
    s[index - W:] creates a suffix of up to O(n) characters, and startswith
    may compare up to m characters.

Space Complexity: O(n)
    The dp array stores one value for every prefix boundary.

dp[index] indicates whether s[:index] can be segmented. dp[0] is true because
the empty prefix needs no words. A word of length W can end at index when the
preceding prefix, dp[index - W], is valid and the suffix beginning there starts
with that word. The final entry represents the entire string.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        S = len(s)

        dp = [0] * (S + 1)
        dp[0] = 1

        for index in range(S + 1):
            for word in wordDict:
                W = len(word)
                if index < W or dp[index - W] == 0:
                    continue
                if s[index - W :].startswith(word):
                    dp[index] = dp[index - W]

        return bool(dp[-1])

"""
Trie-assisted depth-first search over valid word boundaries.

Time Complexity: O(L + n^2)
    - n = len(s)
    - L = the total number of characters in wordDict

    Building the trie takes O(L). Each reachable boundary is processed once,
    but a trie lookup may scan the remaining suffix, giving O(n^2) total work
    in the worst case.

Space Complexity: O(L + n)
    The trie uses O(L) space. The visited array, DFS stack, and a lookup's list
    of matching end positions use O(n) additional space.

startsWith(target, start) follows the trie from target[start:] and returns every
exclusive end index at which a dictionary word finishes. The DFS treats those
indices as the next segmentation boundaries. visited prevents the same boundary
from being added to the stack more than once.
"""
class Trie:
    def __init__(self):
        self.children = dict()
        self.end = False

    def insert(self, target: int):
        node = self

        for ch in target:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]

        node.end = True

    def startsWith(self, target: str, start: int) -> List[int]:
        ans = []
        node = self

        for i in range(start, len(target)):
            ch = target[i]

            if ch not in node.children:
                return ans

            node = node.children[ch]
            if node.end:
                ans.append(i + 1)

        return ans


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        S = len(s)
        t = Trie()
        visited = [False] * (S + 1)

        for word in wordDict:
            t.insert(word)

        stack = [0]

        while stack:
            start = stack.pop()

            starts_with = t.startsWith(s, start)

            for start_index in starts_with:
                if start_index == S:
                    return True
                if visited[start_index]:
                    continue
                visited[start_index] = True
                stack.append(start_index)

        return False
