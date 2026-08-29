class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # 공간복잡도 : 변수 2개 및 상수만 사용하므로, O(1)
        # 시간복잡도 : bit counting한 이후에 n을 1/2하므로 O(logn)
        bit_count = 0
        while n > 0:
            if n % 2 == 1:
                bit_count += 1
            n //= 2
        
        return bit_count
      
