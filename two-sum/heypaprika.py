"""
복잡도 : 예상 -> 예상한 이유

시간 복잡도 : O(n) -> 딕셔너리 키로 검색하는 것은 O(1), 따라서 for 문 1개로 O(n)
공간 복잡도 : O(n) -> n 수 만큼 반복되면서 값이 할당됨.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        n = len(nums)
        
        for i in range(n):
            num_A = nums[i]
            num_B = target - num_A
            if num_B in num_dict:
                return [i, num_dict[num_B]]
            num_dict[num_A] = i
        return []

