class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # 1. n의 마지막 자리를 뽑아서(n & 1)
            # 2. result의 마지막 자리를 0으로 만든 다음(result << 1 -> 마지막 자리가 0)
            # 3. 그 마지막 자리에 n의 마지막 자리를 붙임(0과의 OR 연산)
            result = (result << 1) | (n & 1)
            # n의 자리를 이동
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
