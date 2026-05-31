class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             ans[i] = ans[i] * nums[j]
        # return ans
        # 시간복잡도를 줄이기 위해서 이중루프를 안쓰는 방법으로
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(len(nums) - 1):
            left[i+1] = left[i] * nums[i]
        print(left)
        for j in range(len(nums) - 1, 0, -1):
            right[j-1] = right[j] * nums[j]
        print(right)
        
        answer = []
        for k in range(len(left)):
            answer.append(left[k]*right[k])
        return answer
