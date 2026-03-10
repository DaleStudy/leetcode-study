"""
[결과 요약]
# 재시도횟수: 4회
    1. 모든 문자열 조합을 계산하기(O(n^3))
    2. 중심 확장(O(n^2)): 문자열을 순서대로 순회하며 중심을 기준으로 좌우 대칭 비교"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def _expand_around(left, right) -> tuple[int, int]:
            while left >= 0 and right < length_s and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        # 초깃값
        length_s = len(s)
        best_left, best_right = 0, 0

        # 1. 중심을 한 칸씩 이동하면서 반복하기
        for i in range(len(s)):
            # 2. 짝수/홀수 각각에 대해 탐색하기
            odd_left, odd_right = _expand_around(i, i)
            even_left, even_right = _expand_around(i, i + 1)

            best_length = best_right - best_left
            odd_length = odd_right - odd_left
            even_length = even_right - even_left

            if odd_length > best_length:
                best_left, best_right = odd_left, odd_right
            if even_length > best_length:
                best_left, best_right = even_left, even_right

        return s[best_left : best_right + 1]


"""
#1. 브루트포스(O(n^3)): 순차 탐색하는 비효율적 알고리즘
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
"""


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
