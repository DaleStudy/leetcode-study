"""
[결과 요약]
# 시도한 로직 수: 2
    1. 문자열을 뒤집어 새 객체를 만들기 O(1) / O(1)
        - reversed() 또는 문자열 슬라이싱으로 풀 수 있음
        - 메모리를 많이 사용함
    2. 비트 연산 기반의 코드 O(1) / O(1)
        - 파이썬의 특성으로 인해 (1)에 비해 메모리가 크게 개선되지는 않음
            - 파이썬은 int가 ‘기변 길이’의 객체여서 연산마다 새로운 객체를 생성하기 때문
        - 문자열 생성/파싱 등의 오버헤드가 줄기 때문에 성능에서 약간의 이점이 있음(지금 문제에서 큰 차이 x)
    +) C, C++ 등의 언어는 int가 고정 크기(primitive)이기 때문에 재할당이 줄어서 메모리 사용에 이점이 있음
"""


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
