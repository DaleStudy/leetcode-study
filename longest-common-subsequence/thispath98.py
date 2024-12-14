"""
# Time Complexity: O(N)
- lce_dict 생성: N
- N개의 key에 대하여 순회하면서 값 확인: N
# Space Compelexity: O(k)
- 중복되지 않은 key k개 저장
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lce_dict = {}
        for num in nums:
            lce_dict[num] = True

        answer = 0
        for num in nums:
            cur_lce = 1
            if lce_dict.pop(num, None) is None:
                continue

            down_num = num - 1
            while down_num in lce_dict:
                cur_lce += 1
                lce_dict.pop(down_num)
                down_num -= 1
                
            up_num = num + 1
            while up_num in lce_dict:
                cur_lce += 1
                lce_dict.pop(up_num)
                up_num += 1

            answer = answer if answer > cur_lce else cur_lce

        return answer
