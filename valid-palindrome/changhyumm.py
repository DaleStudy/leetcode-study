class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 시간복잡도 O(n)
        # loop
        s_list = [x.lower() for x in s if x.isalnum()]
        # 시간복잡도 O(n)
        # loop + list pop()
        for i in range(len(s_list)//2):
            if s_list[i] != s_list.pop():
                return False
        return True
