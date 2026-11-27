class Solution:
     # Time: O(n)( for loop 순회 및 reverse) Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        arrange=''
        for elem in s:
            if elem.isalnum(): #처음에 isalpha()로 시도했다가 숫자도 포함해야해서 isalnum()으로 교체
                arrange+=elem
        return arrange==arrange[::-1]
