class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_characters = dict()
        longest_length = 0
        start_idx = 0

        for end_idx, c in enumerate(s):
            if c in used_characters:
                duplicated_idx = used_characters[c]
                if duplicated_idx >= start_idx:
                    start_idx = duplicated_idx + 1

            used_characters[c] = end_idx
            longest_length = max(longest_length, end_idx - start_idx + 1)

        return longest_length


"""
# Set을 이용한 구현(Dict와 복잡도 상으로는 큰 차이 없음)
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
            # 속도는 if문보다 약간 느리지만 가독성 크게 개선
            longest_length = max(longest_length, end_idx - start_idx + 1)

        return longest_length
"""

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
