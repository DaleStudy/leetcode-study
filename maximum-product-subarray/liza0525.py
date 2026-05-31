# 7기 풀이
# 시간 복잡도: O(n)
# - nums의 길이(n)만큼의 시간 복잡도
# 공간 복잡도: O(1)
# - 몇 개의 변수만 사용
class Solution:
    # 문제에서는 이어지는 subarray 내에 음수가 짝수 번 만큼 있다면 최대가 만들어지기도 하므로
    # max_val과 min_val을 가지고 음수의 곱도 대응할 수 있도록 한다. 
    def maxProduct(self, nums: List[int]) -> int:
        max_val, min_val = nums[0], nums[0]
        res = nums[0]

        for num in nums[1:]:
            prev_max_val = max_val  # 이전 max_val은 업데이트 되기 전에 잠시 저장

            # 현재 loop에서 num과 max_val(이전까지의 최대곱) * num과 min_val(이전까지의 최소곱) * num 중
            # 가장 큰 수를 max_val로 업데이트
            # 이때 num이 저장된다는 의미는 최대/최소곱을 해당 숫자에서 다시 시작하여 곱한다는 의미
            max_val = max(num, max_val * num, min_val * num)

            # min_val도 max_val과 동일한 원리로 저장, 이때는 미리 저장한 prev_max_val을 이용
            min_val = min(num, prev_max_val * num, min_val * num)

            # 현재까지의 결과와 이번 loop에서의 max_val을 비교하여 더 큰 수를 res로 업데이트
            res = max(res, max_val)
        
        return res
