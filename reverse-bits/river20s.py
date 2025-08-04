class Solution:
    # -- follow up
    # If this function is called many times, 
    # how would you optimize it?
    # - 클래스 변수로 lookup table 만들어
    # - 8bits 단위로 미리 비트 뒤집은 테이블을 만들어두는 방법
    # _lookup_table_8bit = [0] * 256
    # for i in range(256):
    #     val = i
    #     rev_val = 0
    #     for _ in range(8): # 8비트 뒤집기
    #         rev_val = (rev_val << 1) | (val & 1)
    #         val >>= 1
    #     _lookup_table_8bit[i] = rev_val
    # def __init__(self):
    #     pass

    def reverseBits(self, n: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        - 항상 32번 연산하므로 O(1),
        - 함수가 여러 번 호출되면 누적되어 성능 영향 줄 수도 있음 
        -> reverseBits_lookupTable() 사용
        """
        reversed_n = 0 # 뒤집은 비트 저장
        num_bits = 32 

        for i in range(num_bits):
            reversed_n <<= 1

            if (n & 1) == 1:
                reversed_n |= 1
            
            n >>= 1
        
        return reversed_n

    def reverseBits_lookupTable(self, n: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        - 룩업 테이블 생성 시 공간 필요
        - 하지만 최초 한 번만 필요하므로
        - 호출 누적되면 연산량은 더 적음
        """
        b0 = (n >>  0) & 0xFF  
        b1 = (n >>  8) & 0xFF
        b2 = (n >> 16) & 0xFF
        b3 = (n >> 24) & 0xFF

        rev_b0 = self._lookup_table_8bit[b0]
        rev_b1 = self._lookup_table_8bit[b1]
        rev_b2 = self._lookup_table_8bit[b2]
        rev_b3 = self._lookup_table_8bit[b3]

        result = (rev_b0 << 24) | (rev_b1 << 16) | (rev_b2 << 8) | rev_b3
        
        return result
