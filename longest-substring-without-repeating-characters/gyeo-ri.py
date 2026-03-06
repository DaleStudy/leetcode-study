class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring: str = ""
        current_substring: str = ""

        for c in s:
            if len(longest_substring) < len(current_substring):
                longest_substring = current_substring

            if c not in set(current_substring):
                current_substring += c

            else:
                current_substring = current_substring.split(c)[1] + c

            if len(longest_substring) < len(current_substring):
                longest_substring = current_substring
        return len(longest_substring)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("a", 1),
        ("bb!1  2@!#$1%3", 9),
    ]
    for idx, cases_ in enumerate(test_cases):
        s, answer = cases_
        result = solution.lengthOfLongestSubstring(s)
        assert (
            answer == result
        ), f"Test Case {idx} Failed: Expected {answer}, Got {result}"
