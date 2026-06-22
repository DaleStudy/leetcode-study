# 7기 풀이
# 시간 복잡도: O(n)
#  - nums의 모든 요소를 탐색하기 때문에 nums의 길이에 관련되어 있음
# 공간 복잡도: O(1)
#  - 변수 이외에 객체를 쓰지 않았기 때문에 공간 복잡도는 O(1)이다(input 길이와 상관 없음)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # 1. (현재까지의 합과 i의 요소를 더한 값)과 i의 요소를 서로 비교하여 지금까지의 합을 업데이트한다.
            #  - 자기 자신만으로도 이전 합들보다 크다면 이전 합들은 의미가 없어짐을 얘기
            curr_sum = max(nums[i], curr_sum + nums[i])

            # 현재까지의 합과 이전 max 합을 비교하여 업데이트
            max_sum = max(max_sum, curr_sum)

        return max_sum
