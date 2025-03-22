'''
# 5. Longest Palindromic Substring

DP 테이블을 사용하여 팰린드롬 여부를 저장하고 최대 길이를 찾기.
'''
class Solution:
    '''
    TC: O(n^2)
    SC: O(n^2)
    '''
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        start, length = 0, 1
        dp = [[False] * n for _ in range(n)] # SC: O(n^2)

        # length 1, diagonal elements in 2d array
        for i in range(n): # TC: O(n)
            dp[i][i] = True

        # length 2, are two elements same
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, length = i, 2

        # length 3+
        for word_length in range(3, n + 1): # TC: O(n^2)
            for i in range(n - word_length + 1):
                j = i + word_length - 1

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start, length = i, word_length
                
        return s[start:start + length] 
    
'''
## Check Leetcode Hints
- How can we reuse a previously computed palindrome to compute a larger palindrome?
  - use dp table that stores isPalindrome computation.
- If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
  - if it is palindrome, we only need to check the outermost chars, that wrapping our palindrome.
- Palindromic checks can be O(1) by reusing prev computations.
  - DP!

## 동적 프로그래밍 풀이
- s[i:j]의 팰린드롬 여부를 저장하기 위해서는 2차원 배열을 사용하는 것이 간편하다.
- 길이가 1인 경우, 팰린드롬
- 길이가 2인 경우, 두 문자가 같다면 팰린드롬
- 3 이상은 dp 테이블을 활용하며 확인
  - ex) 길이가 5인 문자열을 다음과 같이 탐색
  ```
  len: 3, i: 0, j: 2
  len: 3, i: 1, j: 3
  len: 3, i: 2, j: 4
  len: 4, i: 0, j: 3
  len: 4, i: 1, j: 4
  len: 5, i: 0, j: 4
  ```

## 탐구
- can we use sliding window to optimize?
슬라이딩 윈도우는 연속적인 구간을 유지하며 최적해를 찾을 때 유용하지만, 팰린드롬은 중앙 확장과 이전 계산 재사용이 핵심.

- can we solve this by counting char?
문자 개수를 세면 "어떤 문자가 몇 번 나왔는지"만 알 수 있지만, 팰린드롬 여부는 문자 순서가 중요하다.

- 그렇다면 개선 방법은? 
> Manacher's Algorithm: https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/  
>
>팰린드롬의 대칭성을 활용해 중앙을 기준으로 확장하는 Manacher's Algorithm을 적용할 수 있다. 모든 문자 사이에 #을 넣어 짝수, 홀수를 동일하게 다루는 기법인데 구현이 다소 복잡하다. 시간 복잡도는 O(n)이다.
'''
class Solution:
    '''
    TC: O(n)
    SC: O(n)
    '''
    def longestPalindromeManacher(self, s: str) -> str:
        '''
        1. 문자열 변환하기 (가운데에 # 추가)
        2. 저장공간 초기화
        3. 변환된 문자열 순회하기
          (a) 미러 인덱스 계산
          (b) 팰린드롬 반지름 확장
            - i에서 양쪽 문자들을 비교해서 확장
          (c) 새로운 팰린드롬 찾기
            - 새로운 팰린드롬을 i로 설정
            - 새로운 팰린드롬의 오른쪽 끝을 i + p[i]로 설정
          (d) 가장 긴 팰린드롬 업데이트
        '''
        transformed = '#' + '#'.join(s) + '#'
        n = len(transformed)
        p = [0] * n # i 중심의 팰린드롬 크기 
        c = 0  # 현재 팰린드롬의 중심
        r = 0  # 현재 팰린드롬의 오른쪽 끝
        max_len = 0  # 가장 긴 팰린드롬의 길이
        center = 0  # 가장 긴 팰린드롬의 중심

        for i in range(n):
            # 현재 위치 i의 미러 인덱스 (중앙을 기준으로 대칭되는 인덱스)
            # ex) ababbaa
            #     0123456
            # i가 3이고 center가 2일 때, 2*2 - 3 = 1, 미러 인덱스는 1
            # i가 5이고 center가 4일 때, 2*4 - 5 = 3, 미러 인덱스는 3
            mirror = 2 * c - i

            if i < r:
                # r - i: 얼마나 더 확장 될 수 있는가 => 현재 팰린드롬의 오른쪽 끝에서 현재 인덱스까지의 거리
                # p[mirror]: 미러 인덱스에서의 팰린드롬 반지름
                p[i] = min(r - i, p[mirror])
                # 작은 값만큼만 확장이 가능하다. 예를 들어, r - i가 더 작은 값이라면 팰린드롬을 그만큼만 확장할 수 있고, p[mirror]가 더 작은 값이라면 이미 그만큼 확장이 된 상태
                # r - i가 3이고 p[mirror]가 2라면 팰린드롬을 2만큼 확장할 수 있고, r - i가 2이고 p[mirror]가 3이라면 팰린드롬을 2만큼 확장할 수 있다.

            # 현재 중심에서 팰린드롬을 확장
            # 양 끝이 같다면 팰린드롬 반지름 p[i]를 1씩 증가
            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and transformed[i + p[i] + 1] == transformed[i - p[i] - 1]:
                p[i] += 1

            # 기존에 찾은 팰린드롬보다 더 큰 팰린드롬을 찾은 경우 
            # 현재 중심과 오른쪽 끝을 설정
            if i + p[i] > r:
                c = i
                r = i + p[i]

            # 가장 긴 팰린드롬 업데이트
            if p[i] > max_len:
                max_len = p[i]
                center = i

        # 변환된 문자열에서 가장 긴 팰린드롬을 원래 문자열에서 추출
        start = (center - max_len) // 2
        return s[start:start + max_len]
