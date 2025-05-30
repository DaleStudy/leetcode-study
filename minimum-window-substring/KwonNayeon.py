"""
Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.

Time Complexity: O(s * t)
- for 루프로 s의 길이만큼 반복
- while 루프 안의 all() 조건에서 t의 각 문자 비교
- 따라서 O(s * t)

Space Complexity: O(s + t)  
- t_counts: O(t)의 공간
- w_counts: O(s)의 공간
- 따라서 O(s + t)

풀이방법:
1. Counter로 t의 문자 빈도수 저장
2. 슬라이딩 윈도우로 s 탐색:
  - high 포인터로 윈도우를 확장하며 필요한 문자 찾기
  - 필요한 문자를 모두 찾으면 low 포인터로 윈도우 축소
3. 최소 길이의 윈도우 반환

메모:
- 관련 문제:
  - Two Sum (딕셔너리)
  - Ransom Note (Counter)
  - Longest Substring Without Repeating (슬라이딩 윈도우)
  - Permutation in String (슬라이딩 윈도우 + Counter)
  - Find All Anagrams in a String (슬라이딩 윈도우 + Counter)
- 4, 5번 문제 먼저 풀어보기
"""
class Solution:
   def minWindow(self, s: str, t: str) -> str:
       
       t_counts = Counter(t)
       w_counts = Counter()
       
       min_low, min_high = 0, len(s)
       low = 0
       
       for high in range(len(s)):
           w_counts[s[high]] += 1
           
           while all(t_counts[ch] <= w_counts[ch] for ch in t_counts):
               if high - low < min_high - min_low:
                   min_low, min_high = low, high
               if s[low] in t_counts:
                   w_counts[s[low]] -= 1
               low += 1
               
       return s[min_low : min_high + 1] if min_high < len(s) else ""
