class Solution:
    def reverseBits(self, n: int) -> int:
        n_binary_str = bin(n).replace("0b", "").zfill(32)
        n_reversed_binary = "".join(reversed(n_binary_str))
        return int(n_reversed_binary, 2)


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
