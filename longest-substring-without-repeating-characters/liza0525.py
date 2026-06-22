# 7기 풀이
# 시간 복잡도: O(n)
# - 슬라이딩 윈도우 기법을 사용, s의 길이 n에 비례
# 공간 복잡도: O(min(n, k))
# - 중복 문자를 저장 및 체크할 char_set의 최대 크기인 k(s의 모든 문자가 중복하지 않을 때)와 s의 크기 n 중 작은 쪽
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0  # 왼쪽 포인터 지정
        char_set = set()  # 중복 문자 체크를 위한 set 추가

        # right를 하나씩 옮겨가며 문자열 길이를 체크,
        for right in range(len(s)):
            while s[right] in char_set:
                # 중복 문자가 생길 경우 left를 움직이되, 중복된 문자 이전의 모든 문자를 제한다.
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])  # 현재의 문자인 s[right]를 char_set에 저장하여 다음 루프에 중복 체크를 하도록 한다.
            max_len = max(max_len, right - left + 1)  # 현재까지의 가장 긴 문자열을 계산하여 max_len 업데이트

        return max_len
