# TC: O(n), 최대 n번 실행
# SC: O(n), 최대 n 길이의 리스트
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_acc_product = [0 for i in range(len(nums))]
        right_acc_product = [0 for i in range(len(nums))]
        
        length = len(nums)
        last_index = length - 1

        for i in range(length):
            left_acc_product[i] = (left_acc_product[i - 1] if i > 0 else 1) * nums[i]
            right_acc_product[last_index - i] = right_acc_product[last_index - i + 1] * nums[last_index - i] if last_index - i != last_index else nums[last_index - i]
        
        result = [0 for i in range(length)]
        for i in range(length):
            if i == 0:
                result[i] = right_acc_product[i + 1]
            elif i == last_index:
                result[i] = left_acc_product[i - 1]
            else:
                result[i] = left_acc_product[i - 1] * right_acc_product[i + 1]

        return result

