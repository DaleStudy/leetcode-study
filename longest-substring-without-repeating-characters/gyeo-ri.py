"""
[결과 요약]
# 재시도횟수: 4회
    1. 모든 문자열 한 번씩 순회하기(실패)
        - 단순 순회가 아니라 실패 시 직전의 중복 문자열 위치를 찾아야 해서 단순 순회로는 처리가 불가함
    2. 문자열 상태를 기록하고, 중복된 문자열이 등장했을 때 기존 문자열을 split 하여 다시 순회를 시작하는 방법(힌트 없이 성공한 방식)
        - 연산 결과는 동일하지만 복잡도가 O(n^2)으로 효율적이지는 않음
    (3부터 구현 방식에 대한 힌트를 참조)
    3. Sliding Window를 구현(두 개의 포인터, Set)
         - 시간복잡도: O(n) / 공간복잡도: O(n)
        - 중복 발생 시 while문을 사용하여 중복된 문자가 등장하는 위치까지 순차 탐색(이전 문자열을 제거)
    4. Dict으로 (3)과 같은 로직을 구현
         - 시간복잡도: O(n) / 공간복잡도: O(n)이지만 dict을 사용하므로 시간 절약 / 메모리는 약간 더 사용함
        - 인덱스를 순차로 탐색하는 것이 아니라 dict에서 바로 조회하는 방식


"""


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
