
"""
Solution: 
    1) bin() 메서드로 binary 만들어주고 
    2) 1 의 갯수를 세어준다.
Time: O(n^2)
Space: O(1)
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0 for i in range(n + 1)]

        for i in range(n+1):
            b = bin(i)
            count = 0
            for char in b:
                if char == '1':
                    count += 1
            result[i] = count
        
        return result
    
"""
Solution: 
    1) 2로 나눈 나머지가 1bit 이라는 성질을 이용해서 count
Time: O(n logn)
Space: O(1)
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(num):
            count = 0
            while num > 0:
                count += num % 2 
                num = num // 2
            return count
        
        return [count(i) for i in range(n+1)]

"""
Solution:
    1) LSB 가 0 1 0 1 반복되므로 num % 2 를 사용한다.
    2) 나머지 빗은 LSB를 제외한 값이므로 num // 2 를 사용한다.
Time: O(n)
Space: O(1)
"""

class Solution:
    
    def countBits(self, n: int) -> List[int]:
        dp = [0 for i in range(n+1)]

        for i in range(1, n+1):
            LSB = i % 2
            dp[i] = dp[i // 2] + LSB

        return dp
