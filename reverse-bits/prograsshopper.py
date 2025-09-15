class Solution:
    def reverseBits(self, n: int) -> int:
        stack_n = []
        while len(stack_n) < 32:
            stack_n.append((n % 2))
            n //= 2

        result = 0
        scale = 1

        while stack_n:
            result += stack_n.pop() * scale
            scale *= 2

        return result
