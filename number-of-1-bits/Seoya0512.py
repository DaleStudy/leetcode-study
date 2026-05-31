'''
Approach 
- 십진법을 이진법으로 변환하는 방식과 누적합을 사용함

Time Complexity: O(log n)
- while 문에서 숫자(num)을 계속해서 2로 나누는데 소요되는 시간

Space Complexity: O(1)
- 상수 bits와 nums를 저장하는 공간
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        # 주어진 숫자를 2로 나눈 나머지 값이 1인 경우 bits에 누적함 
        num = n
        while num != 0 : 
            if num % 2 == 1 :
                bits += 1
            num //= 2
        return bits
