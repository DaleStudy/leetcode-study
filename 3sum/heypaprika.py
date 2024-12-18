# 2Sum을 활용한 풀이
# Note : 정렬 후 푸는 것이 더 직관적이고, 빠름

"""
복잡도 : 예상 -> 예상한 이유

시간 복잡도 : O(n^2) -> nums 배열 2중 for문
공간 복잡도 : O(n) -> 최악의 경우 nums 배열 길이만큼의 딕셔너리 생성
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_list = set()
        added_pair = {}
        for target_i, target_number in enumerate(nums):
            cur_ans_list = []
            num_dict = {}
            if target_number in added_pair:
                continue

            for i in range(target_i + 1, len(nums)):
                num_A = nums[i]
                num_B = - target_number - num_A
                if num_B in num_dict:
                    cur_ans_list.append(sorted([target_number, num_A, num_B]))
                    added_pair[target_number] = num_A
                num_dict[num_A] = 1
            for item in cur_ans_list:
                ans_list.add(tuple(item))
        return list(ans_list)

