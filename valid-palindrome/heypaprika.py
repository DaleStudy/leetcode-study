# Big-O 예상 : O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.lower().split(" "))
        new_s = ""
        for item in s:
            if (ord("a") <= ord(item) <= ord("z")) or (ord("0") <= ord(item) <= ord("9")):
                new_s += item
        output = True
       new_s_2 = new_s[::-1]
        return new_s_2 == new_s
        return output

