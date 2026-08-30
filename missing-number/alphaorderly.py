"""
시간복잡도: O(n)
공간복잡도: O(1)

'target'을 배열의 길이(n)로 설정한 뒤, 0부터 n-1까지의 인덱스와 배열의 모든 값을 xor 연산합니다.
이 과정을 거치면, 배열과 인덱스 모두에 존재하는 값은 xor 연산으로 소거되어 사라집니다(x ^ x = 0).
최종적으로 남는 값이 배열에 존재하지 않는 누락된 숫자가 됩니다.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = len(nums)
        for i, v in enumerate(nums):
            target ^= i ^ v
        return target