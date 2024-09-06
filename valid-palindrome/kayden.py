# 시간복잡도: O(N)
# 공간복잡도: O(N)
class Solution:

    def isPalindrome(self, s: str) -> bool:
        string = ""

        for letter in s:
            if letter.isalnum(): # if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
                string += letter.lower()


        def valid(s):
            start, end = 0, len(s)-1

            while start < end:
                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1

            return True

        return valid(string)
