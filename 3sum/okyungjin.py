# [문제 링크]
# https://leetcode.com/problems/3sum/

# [요구사항]
# - nums 배열이 주어지고, nums[i] + nums[j] + nums[k] 를 더했을 때 0이 는 숫자 3개의 배열을 반환한다.
# - 결과 집합은 1개 이상임
# - 정답에 중복이 있으면 안 된다!
# - `3 <= nums.length <= 3000`

# [접근법]
# 1. 포인터를 3개 선언하고, 하나를 고정한 채로 2Sum으로 나머지 해를 찾는다.
# 2. 중복 제거를 위해 포인터를 좌우로 움직여줘야 한다.

# 시간 복잡도: O(N^2)
# 공간 복잡도: O(N)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        size = len(nums)
        answer = []

        # 포인터를 사용하기 위해 배열을 정렬한다
        nums.sort()

        # 포인터 3개 중 하나를 고정한다.
        for i in range(size - 2):
            # 중복 제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 나머지 두 개의 포인터를 left, right라 한다. 양 끝을 할당
            left = i + 1
            right = size - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # 합이 0보다 작으면 더 큰 숫자를 더해줘야 하므로 left를 우측으로 이동
                if total < 0:
                    left += 1

                # 합이 0보다 크면 더 작은 숫자를 더해줘야 하므로 right을 좌측으로 이동
                elif total > 0:
                    right -= 1

                # 숫자 3개가 합쳐서 0인 경우 (해를 찾음)
                else:
                    # 정답에 추가하고
                    answer.append([nums[i], nums[left], nums[right]]) 

                    # 포인터를 안쪽으로 한칸 이동한다.
                    left += 1
                    right -= 1

                    # left 중복 제거를 위해 이동
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # right 중복 제거를 위해 이동
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return answer
