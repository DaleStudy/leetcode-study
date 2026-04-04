"""
[결과 요약]
# 시도한 로직 수: 2
    1. if/else 문으로 분기 처리(시간: O(n) / 공간: O(1))
        -
    2. if문 대신 min / max를 계속 계산하는 로식
        - None 대신 float(inf)를 사용하여 None 검증 분기 제거
        - inf 사용을 위해서 마지막 return에 int() 타입 변환 필요
        - 성능은 1과 큰 차이 없으며 코드가 간소화
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float("inf")

        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)

        return int(max_profit)


if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
        ([1, 2, 4, 10000, 2, 1, 3], 9999),
    ]

    solution = Solution()
    for idx, case_ in enumerate(test_cases):
        prices, answer = case_
        result = solution.maxProfit(prices)
        assert (
            answer == result
        ), f"Test Case {idx} Failed: Expected {answer}, Got {result}"
