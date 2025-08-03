class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 배열 정렬해서 중복 처리와 투 포인터에 유리하게 만듦
        n = len(nums)
        answer = []

        for i in range(n - 2):
            # i가 0이 아니면서 이전 값과 같으면 중복 방지를 위해 건너뜀
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    answer.append([nums[i], nums[left], nums[right]])

                    # left와 right가 가리키는 값이 중복이면 넘어감
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return answer

        