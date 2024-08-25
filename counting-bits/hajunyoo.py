class Solution1:
    # time complexity: O(n)
    # space complexity: O(1)
    def countBits(self, n: int) -> List[int]:
        list = [i for i in range(n + 1)]
        result = [bin(num).count('1') for num in list]
        return result

class Solution2:
    # time complexity: O(n * logn)
    # space complexity: O(1)
    def countBits(self, n: int) -> List[int]:

        def count(num):
            cnt = 0
            while num:
                cnt += num % 2
                num //= 2
            return cnt

        res = [count(i) for i in range(n+1)]
        return res

class Solution3:
    # time complexity: O(n)
    # space complexity: O(1)
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        msb = 1
        for i in range(1, n + 1):
            if i == msb * 2:
                msb *= 2
            res[i] = res[i - msb] + 1
        return res
