"""
# Time Complexity: O(N)
- N개의 char를 각각 한번씩 순회
# Space Compelexity: O(N)
- 최악의 경우 (공백이 없을 경우) N개의 char 저장
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [char.lower() for char in s if char.isalnum()]
        for i in range(len(string) // 2):
            if string[i] != string[-i - 1]:
                return False
        return True
