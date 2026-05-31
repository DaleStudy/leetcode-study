"""
# Intuition
처음에는 1주차의 Two Sum 문제 풀이를 응용하여, 배열 순회 + 해시 테이블 만들어 값 찾기를 시도했으나
정렬 + 투포인터 풀이가 더 빠르므로 그렇게 제출했습니다.

# Approach
nums 배열을 순회하면서 -nums[i]를 합으로 하는 두 수를 나머지 배열 부분에서 찾는다.
찾을 때는 정렬 & 투포인터를 활용하여 중복을 건너 뛰는 방식으로 속도를 높인다.


# Complexity
- Time complexity: 정렬 + 투포인터 이중 반복으로 O(N^2)

- Space complexity: 정렬 하는데에 O(N) , answer 배열 생성하는데에 O(M)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # O(NlogN)
        n = len(nums)
        answer = []

        for i in range(n - 2):  # 이중 반복문 O(N^2)
            # 중복 제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # nums[i]가 0보다 크면 뒤도 다 양수라 종료 가능
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # left/right 중복 제거
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return answer
