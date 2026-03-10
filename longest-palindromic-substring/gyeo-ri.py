class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                subset = s[i : j + 1]

                if subset == subset[::-1]:
                    if len(answer) < len(subset):
                        answer = subset
        return answer


if __name__ == "__main__":
    test_cases = [
        ("babad", ["bab", "aba"]),
        ("bb", ["bb"]),
        ("aaabaaa", ["aaabaaa"]),
        ("c", ["c"]),
        ("123a24542a0321", ["a24542a"]),
    ]

    solution = Solution()
    for idx, case_ in enumerate(test_cases):
        s, answers = case_
        result = solution.longestPalindrome(s)
        assert (
            result in answers
        ), f"Test Case {idx} Failed: Expected one of {",".join(answers)}, Got {result}"
