class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lower_text = s.lower()
        # clean_text = re.sub(r'[^a-z0-9]', '', lower_text)
        # if len(clean_text) ==0:
        #     return True
        
        # j = len(clean_text) - 1
        # ans = True

        # for i in range(len(clean_text) // 2):
        #     if clean_text[i] != clean_text[j]:
        #         ans = False
        #         break
        #     j -= 1
        # return ans
        n = "".join(c for c in s if c.isalnum()).lower()
        return n == n[::-1]            


