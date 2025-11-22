# 2차 시도: 왼쪽 누적 곱 * 오른쪽 누적 곱
# 시간 복잡도: O(n), for문 사용
# 공간 복잡도: O(n), 길이 n인 리스트 prefix, suffix, result 생성
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 왼쪽 누적 곱 리스트 생성
        prefix = [nums[0]]
        for i in range(1, len(nums)-1):
            tmp = nums[i]
            prefix.append(prefix[i-1] * nums[i])

        nums.reverse()
        # 오른쪽 누적 곱 리스트 생성
        suffix = [nums[0]]
        for i in range(1, len(nums)-1):
            tmp = nums[i]
            suffix.append(suffix[i-1] * nums[i])

        # result[0] = suffix[2]
        # result[1] = suffix[1] * prefix[0]
        # result[2] = suffix[0] * prefix[1]
        # result[3] =             prefix[2]
        result = [0 for i in range(0, len(nums))]
        result[0] = suffix[-1]
        result[-1] = prefix[-1]
        for i in range(1, len(nums)-1):
            result[i] = suffix[len(nums)-2-i] * prefix[i-1]
        return result


# 1차 시도: 이중 for문 사용
# 시간 복잡도: O(n^2)으로 실패
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in range(0, len(nums)):
#             tmp = 1
#             for j in range(0, len(nums)):
#                 if i == j:
#                     continue
#                 tmp *= nums[j]
#             result.append(tmp)
#         return result