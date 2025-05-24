"""
Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

<Solution 2>

Time Complexity: O(n²)
- 외부 for문: n번 실행
- 내부 함수 (expand_around_center): 최악의 경우 n번 확장
- 결과: n * n = O(n²)

Space Complexity: O(1)
- 상수 공간만 사용 (count, left, right)

풀이 방법:
1. expand_around_center 헬퍼 함수:
  - 주어진 중심에서 양쪽으로 확장하며 팰린드롬의 개수를 셈
  - 경계 체크, 문자 일치여부 확인
  
2. 각 위치에서 두 가지 경우 확인:
  - 홀수 길이: expand_around_center(i, i) - 중심이 한 글자
  - 짝수 길이: expand_around_center(i, i+1) - 중심이 두 글자

핵심 아이디어:
- 중심에서 바깥으로 확장 (안에서 밖으로)
- 모든 가능한 중심점에서 팰린드롬 탐색

노트:
- dp로도 풀어보기
"""
# Solution 1: Brute-force
class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindromic(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start, end = start + 1, end - 1
            return True

        cnt = 0

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if isPalindromic(i, j):
                    cnt += 1
        return cnt

# Solution 2
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_around_center(left, right):
            cnt = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt

        total = 0

        for i in range(len(s)):
            # 홀수일 때
            total += expand_around_center(i, i)
            # 짝수일 때
            total += expand_around_center(i, i+1)
        
        return total

