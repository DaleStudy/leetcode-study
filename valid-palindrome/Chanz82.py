class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 공간 복잡도 : 문자열의 길이만큼만 공간을 사용합니다. 따라서 O(n)
        # 시간 복잡도 : 문자열의 길이 만큼 순회를 1번 하고, 이후에 한번 더 순회를 하나 길이의 1/2 까지만 순회를 합니다. O(n)
        alpha_num_str = ""
        for ch in s:
            if ch.isalnum():
                alpha_num_str += ch.lower()

        end_idx = len(alpha_num_str) - 1
        for idx, ch in enumerate(alpha_num_str):
            if idx >= end_idx:
                return True
            if ch != alpha_num_str[end_idx]:
                return False
            end_idx -= 1
        return True
      
