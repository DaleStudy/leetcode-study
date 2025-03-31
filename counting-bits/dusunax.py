'''
# 338. Counting Bits

0부터 n까지의 이진수에서 1의 개수 세기

## 풀이A. 브루투포스
- 전부 계산하기

## 풀이B. DP
```
이진수 = (이진수 >> 1) + (이진수 & 1)
```
- `i >> 1`: i의 비트를 오른쪽으로 1비트 이동(맨 오른쪽 한 칸 버림), `i // 2`와 같음
- `i & 1`: `i`의 마지막 비트가 1인지 확인 (1이면 1 추가, 0이면 패스)
- DP 테이블에서 이전 계산(i >> 1) 결과를 가져와서 현재 계산(i & 1) 결과를 더한다.
'''
class Solution:
    '''
    A. brute force
    SC: O(n log n)
    TC: O(n)
    '''
    def countBitsBF(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1): # TC: O(n)
            result.append(bin(i).count('1')) # TC: O(log n)
        
        return result

    '''
    B. DP
    SC: O(n)
    TC: O(n)
    '''
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1): # TC: O(n)
            dp[i] = dp[i >> 1] + (i & 1) # TC: O(1)
            
        return dp
