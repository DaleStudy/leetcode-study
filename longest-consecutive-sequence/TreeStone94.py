class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = []
        count = 0
        pre_num = -9999999999999999999
        for n in sorted(set(nums)):
            if pre_num + 1 == n:
                count += 1
            else:
                answer.append(count)
                count = 0
            pre_num = n

        if count != 0:
            answer.append(count)

        if answer:
            return max(answer) + 1
        else:
            return 0
