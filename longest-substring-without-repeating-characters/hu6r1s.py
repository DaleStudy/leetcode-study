class Solution:
    """
    a       => 세트 {}에 a 없음
    ab      => 세트 {a}에 b 없음
    aba     => 세트 {a, b}에 a 있음 => 중복
    abac    => 더 이상 고려 가치 없음
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for start in range(len(s)):
            chars = set()
            for end in range(start, len(s)):
                if s[end] in chars:
                    break
                chars.add(s[end])
                max_len = max(end - start + 1, max_len)
        return max_len
