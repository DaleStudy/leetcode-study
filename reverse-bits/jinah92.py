# O(1) time, O(1) space
class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []
        while len(stack) < 32:
            stack.append(n % 2)
            n //=2
        
        result, scale = 0, 1
        while stack:
            result += stack.pop() * scale
            scale *= 2
        
        return result
