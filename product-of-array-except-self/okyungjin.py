# [요구사항]
# 정수배열 nums가 주어진다.
# answer[i]는 nums[i]를 제외한 나머지 숫자의 곱이다.
# answer 배열을 반환한다.
# 단, 나눗셈 없이 O(N)으로 알고리즘을 작성해야한다.

# [접근법]
# 처음에는 조합(combinations)으로 모든 경우를 구하려 했지만
# 시간 복잡도가 O(N²) 이상이 되어 시간 초과가 발생했습니다.

# (고민해보다가 AI의 도움을 받아 힌트를 얻었습니다.)
# 각 위치에서 왼쪽 누적 곱(prefix)과 오른쪽 누적 곱(suffix)을 각각 구해 곱하는 방식으로 풀었습니다.

# 예시)
# nums = [1, 2, 3, 4]
# prefix = [1, 1, 2, 6] -> 각 위치의 왼쪽 원소들의 곱
# suffix를 뒤에서부터 누적하면서 answer에 곱해줍니다.
# 최종 answer 배열 [24, 12, 8, 6]

# 시간 복잡도 : O(N)
# 공간 복잡도 : O(1) (정답 배열 제외)
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)

        answer = []

        prefix = 1
        for i in range(size):
            answer.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for j in reversed(range(size)):
            answer[j] *= suffix
            suffix *= nums[j]

        return answer

print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([2,5,3,7]))
