class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_characters = set()
        longest_length = 0
        start_idx = 0

        for end_idx in range(len(s)):
            while s[end_idx] in used_characters:
                used_characters.remove(s[start_idx])
                start_idx += 1

            used_characters.add(s[end_idx])
            current_length = end_idx - start_idx + 1
            if current_length > longest_length:
                longest_length = current_length

        return longest_length


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
