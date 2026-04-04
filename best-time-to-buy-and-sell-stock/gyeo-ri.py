class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy_at = None

        for p in prices:
            if buy_at is None:
                buy_at = p
            elif buy_at > p:
                buy_at = p
            elif buy_at < p:
                max_profit = max(max_profit, p - buy_at)

        return max_profit


if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
    ]

    solution = Solution()
    for idx, case_ in enumerate(test_cases):
        prices, answer = case_
        result = solution.maxProfit(prices)
        assert (
            answer == result
        ), f"Test Case {idx} Failed: Expected {answer}, Got {result}"
