class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


if __name__ == "__main__":
    test_cases = [
        (43261596, 964176192),
        (2147483644, 1073741822),
        (0, 0),
        (2, 1073741824),
    ]
    solution = Solution()

    for idx, (inp, expected) in enumerate(test_cases, start=1):
        result = solution.reverseBits(inp)
        assert (
            result == expected
        ), f"Test Case {idx} Failed: Expected {expected}, Got {result}"
    print("All test cases passed.")
