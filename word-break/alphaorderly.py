"""
Time Complexity: O(n * k * m)
    - n = len(s)
    - k = number of words in wordDict
    - m = average word length in wordDict

    At each index in s, we may check every word in wordDict and for each, compare up to m characters.

Space Complexity: O(n)
    - n = len(s), due to recursion stack and memoization table (one entry per possible starting index).

- Uses top-down dynamic programming with memoization (via lru_cache).
- The helper function dp(index) returns True if s[index:] can be fully segmented into words from wordDict.
- Base case: If index == len(s), then the entire string is successfully segmented.
- For each call, iterate through all words in the dictionary and check if s[index:] begins with that word.
- If a match is found, recursively check for the remainder of the string starting after the matched word.
- Return True as soon as any valid segmentation is found.
- Return False if no segmentation is possible for this index.
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
Time Complexity: O(n * k * m)
    - n = len(s)
    - k = number of words in wordDict
    - m = average word length in wordDict

    For every index in s, we consider each word in wordDict and, for each, match up to m characters.

Space Complexity: O(n)
    - n = len(s), required for the dp array.

- Uses bottom-up dynamic programming.
- The dp array indicates whether a prefix of s up to index can be segmented into words from wordDict.
- Base case: dp[0] = 1, since the empty string can always be segmented.
- For each index, iterate through all words, and for each, check if s[index - W : index] equals the word, assuming index >= W and dp[index - W] is True.
- If a match is found, update dp[index] to reflect that segmentation.
- Finally, return True if dp[-1] is set, indicating the entire string can be segmented; otherwise, return False.
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
