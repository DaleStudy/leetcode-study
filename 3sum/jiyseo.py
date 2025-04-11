class Solution(object):
    def threeSum(self, nums):
        # 시간복잡도 = O(N^3)
        # length = len(nums)
        # result = []
        # for i in range(length - 1) :
        #     for j in range(i + 1, length) :
        #         s = - (nums[i] + nums[j])
        #         if s in nums[j + 1 : length] :
        #             result.append(sorted((nums[i], nums[j], s)))
        
        # return(list(set(map(tuple, result))))

        # 시간 복잡도 = O(N^2)
        nums.sort()
        length = len(nums)
        result = []

        for i in range(length - 2) :
            if i > 0 and nums[i - 1] == nums[i] : # 같은 숫자인 경우 패스
                continue
            target = nums[i]
            left = i + 1
            right = length - 1

            while left < right :
                sum = target + nums[left] + nums[right]
                if sum > 0 :
                    right -= 1
                elif sum < 0 : 
                    left += 1
                else :
                    result.append([target, nums[left], nums[right]])
                    # 중복 숫자 건너뛰기
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    right -= 1
                    left += 1
                    
        return result

