class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.lower().split(" "))
        new_s = ""
        for item in s:
            if (ord("a") <= ord(item) <= ord("z")) or (ord("0") <= ord(item) <= ord("9")):
                new_s += item
        output = True
        for i in range(len(new_s) // 2):
            if new_s[i] != new_s[-i-1]:
                output = False
                break
        return output

