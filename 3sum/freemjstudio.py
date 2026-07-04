class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort() 
    
        for i in range(len(nums)):
            # 중복된 원소가 있는 경우 똑같이 검사할 필요가 없으므로 건너뛴다.
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            left, right = i+1, len(nums) - 1

            while left < right: 
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    # left, right 포인터를 둘다 한칸씩 이동시켜 다음 조합을 검사한다.
                    left += 1
                    right -= 1

                    # 중복된 원소가 있는 경우 같은 정답 조합을 방지한다 
                    while left < right and nums[left] == nums[left -1]:
                        left += 1

                elif total < 0:
                    left += 1
                else: 
                    right -= 1
        return answer 