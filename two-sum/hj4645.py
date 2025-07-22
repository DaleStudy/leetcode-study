class Solution:
    # 2개의 수를 합해 target이 되는 경우를 찾는 문제
    # 순서가 보장되는 python dictionary를 사용해서,
    # 요소 x에 대해서 target-x 가 딕셔너리 내에 있는지를 찾는다.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in dict:
                return [dict[remain], i]
            dict[num] = i
