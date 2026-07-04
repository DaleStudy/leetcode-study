# TC: O(N^2)
# SC: O(N)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        cnt_dict = Counter(nums)
        nums_uniq = sorted(cnt_dict.keys())
        n = len(nums_uniq)

        ret = []

        for num in cnt_dict.keys():
            if num == 0:
                if cnt_dict[num] >= 3:
                    ret.append([0, 0, 0])
            elif cnt_dict[num] >= 2 and num * 2 * -1 in cnt_dict:
                ret.append([num, num, num * 2 * -1])

        for idx1, num1 in enumerate(nums_uniq):
            if num1 > 0:
                break

            for idx2 in range(idx1 + 1, n):
                num2 = nums_uniq[idx2]
                num3 = (num1 + num2) * -1

                if num2 >= num3:
                    break
                elif num3 in cnt_dict:
                    ret.append([num1, num2, num3])

        return ret

