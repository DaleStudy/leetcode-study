'''
방식 : Brute-Force
문자에 two-pointer를 지정해서 모든 경우의 수를 확인하고
palindrome의 수를 반환

Time Complexity : O(N^3)
- outer loop(For문) : O(N)
- inner loop(While문) : O(N)
- palindrome 확인을 위해 s[start:end] 슬라이싱 및 역순 확인 : O(N)

Space Complexity: O(N)
- substring을 임시 저장하는데 드는 공간 비용
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)

        for start in range(n):
            end = n
            while start < end:
                sub = s[start:end]
                if sub == sub[::-1]:
                    cnt += 1
                end -= 1

        return cnt

'''
위 풀이로 해결했지만, 시간복잡도가 많이 드는 것을 파악 후
알고달레 풀이 3: Two Pointers 이해하고 작성한 코드

while 문을 2회로 나눈 이유는 aa, baab 형식의 짝수 palindrome을 파악하기 위함
짝수 palindrome의 경우 양 옆의 값이 동일해야 그 값을 기준으로 좌우 값을 비교해서 판단할 수 있음
'''
def countSubstrings(s: str) -> int:
  cnt = 0

  for i in range(0, len(s)):
    start, end = i,i
    while start >= 0 and end < len(s) and s[start] == s[end]:
      cnt += 1
      start -=1
      end +=1

    start, end = i, i+1
    while start >= 0 and end < len(s) and s[start] == s[end]:
      cnt += 1
      start -=1
      end +=1

  return cnt
