# 시간 복잡도: O(n)
# - nums를 순회하며 dictionary 생성 O(n)
# - nums를 한 번 더 순회하며 target 탐색 O(n)
# 공간 복잡도: O(n)
# - 각 숫자의 index를 저장하는 dictionary idx_map이 최대 n개의 원소를 가짐

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 요소가 어떤 index값을 가지는지 매칭한 dictionary
        idx_map = {
            el: idx
            for idx, el in enumerate(nums)
        }

        for idx, num in enumerate(nums):
            # target를 만드는, num과 짝이 되는 수를 result_num으로 계산
            result_num = target - num 
            if result_num in idx_map and idx != idx_map[result_num]:
                # 문제의 조건에 맞는 경우에 각 숫자의 index 정보를 early return
                # 문제 조건에 무조건 한 가지 경우만 있다고 했기 때문에 early return해도 된다.
                return [idx, idx_map[result_num]]
