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
    s = Solution()
    print(s.lengthOfLongestSubstring("a"))
