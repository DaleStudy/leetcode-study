class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        # 정렬
        nums.sort()

        for i in range(len(nums)-2):
            # i 중복제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    answer.append([nums[i],nums[left],nums[right]])

                    # left 중복제거
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # right 중복제거
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return answer
