# 비트 풀이
# Time: O(log n) - n의 비트 수만큼 반복, Space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n> 0:
            num += n & 1  # 가장 우측 비트가 1이면 +1 (n % 2)
            n >>= 1       # >>로 right shift (n //= 2)
        return num



# #1번째 풀이
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         num=0
#         # Time: O(log n):n의 비트수만큼 Space: O(log n) :stack이 쌓임
#         #2로 계속 나누면서 나머지를 세는 방식
#         def bin(n):
#             nonlocal num
#             if n==0: #더 이상 나눌 수 없을때까지
#                 return
#             num+=n%2 
#             n//=2
            
#             bin(n)
#         bin(n)
#         return num
