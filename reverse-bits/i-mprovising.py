class Solution:
    """
    Time, space complexity O(1)
    """
    def reverseBits(self, n: int) -> int:
        stack = []
        while len(stack) < 32:
            stack.append(n % 2)
            n //= 2

        reverse, x = 0, 1 
        while stack:
            reverse += stack.pop() * x
            x *= 2
        
        return reverse
