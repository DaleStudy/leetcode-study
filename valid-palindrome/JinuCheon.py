# two point 풀이.
# 시간복잡도: O(n)
# 이중루프라서 시간복잡도 계산이 조금 헷갈린다.
# 추가공간을 쓰지 않는다.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftCursor = 0
        rightCursor = len(s) - 1

        while leftCursor < rightCursor:
            while leftCursor < rightCursor and not s[leftCursor].isalnum():
                leftCursor += 1

            while leftCursor < rightCursor and not s[rightCursor].isalnum():
                rightCursor -= 1
            
            if s[leftCursor].lower() != s[rightCursor].lower():
                return False
            
            leftCursor += 1
            rightCursor -= 1
        
        return True

# 다른 풀이.
# 문자열 클리닝 & 뒤집어서 동등비교를 함.
# 간결하지만 추가공간 사용 -> 공간 O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
