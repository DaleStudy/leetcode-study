# 시간복잡도: O(N)
# 공간복잡도: O(N)
class Solution:

    def isPalindrome(self, s: str) -> bool:
        string = ""

        for letter in s:
            if letter.isalnum():
                string += letter.lower()


        def valid(s):
            st, en = 0, len(s)-1

            while st < en:
                if s[st] != s[en]:
                    return False

                st += 1
                en -= 1

            return True

        return valid(string)
