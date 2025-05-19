"""
Constraints:
- The input must be a binary string of length 32

<Solution 1>

Time Complexity: O(1)
- 항상 고정된 32비트 문자열에 대해 연산하므로 상수 시간
    
Space Complexity: O(1)
- 32비트 고정 크기의 문자열 연산만 사용하므로 상수 공간

풀이 방법:
1. format(n, '032b')를 사용해 입력받은 정수를 32비트 이진수 문자열로 변환함
2. 문자열 슬라이싱 [::-1]으로 비트를 뒤집음
3. int(reversed_binary, 2)로 뒤집은 이진수 문자열을 다시 정수로 변환함
"""

class Solution:
    def reverseBits(self, n: int) -> int:

        binary = format(n, '032b')

        reversed_binary = binary[::-1]
        
        return int(reversed_binary, 2)
"""
<Solution 2>

Time Complexity: 

Space Complexity: 

풀이 방법:
"""
