class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sol 1
        # time complexity: O(n^2) / memory complexity: O(n)
        if len(s) in [0, 1]:
            return len(s)

        from collections import defaultdict
        strings = []
        for i in range(0, len(s) - 1):
            char_dict = defaultdict(int)
            char_dict[s[i]] += 1
            for j in range(i + 1, len(s)):
                char_dict[s[j]] += 1
                if char_dict[s[j]] > 1:
                    strings.append(s[i:j])
                    break
            else:
                strings.append(s[i:])

        max_len = len(strings[0])
        for elem in strings:
            max_len = max(max_len, len(elem))
        return max_len

        # sol 2
        # time complexity: O(n) / memory complexity: O(n)
        str_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in str_set:
                str_set.remove(s[left])
                left += 1
            str_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
