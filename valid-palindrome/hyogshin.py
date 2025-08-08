'''
풀이
- alphanumeric만 저장하는 alnum 배열 생성
- alnum 배열의 절반 (소수점 버림) 길이를 순회하며 Palindrome 인지 확인

시간 복잡도: O(n)
- for loop * 2 -> O(2n) => O(n)

공간 복잡도: O(n)
- alphanumeric만 저장하는 alnum 배열이 최악의 경우 O(n) 일 수 있음
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = []
        is_pal = True
        for c in s:
            if c.isalnum():
                alnum.append(c.lower())
        
        for c in range(len(alnum) // 2):
            if alnum[c] != alnum[-1 - c]:
                is_pal = False
                break
        
        return is_pal
        