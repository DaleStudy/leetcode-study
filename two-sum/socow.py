# 1. 일단 딕셔너리(num_map)를 만들어서 숫자랑 인덱스를 저장한다.
# 2. 현재 숫자와 target을 뺀 결과(보충값, complement)를 계산한다.
# 3. 그 complement가 이미 딕셔너리에 있다면?
#    → 그 숫자와 현재 숫자가 합쳐서 target이 된다는 뜻!
# 4. 없다면 현재 숫자를 딕셔너리에 저장해서 다음에 대비한다.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
