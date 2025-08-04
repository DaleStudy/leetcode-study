class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        all_multi = 1
        zero_count = 0
        result = []

        for v in nums:
            if v == 0:
                zero_count += 1
                continue
            all_multi *= v
        all_multi = int(all_multi)

        if zero_count == 0:
            for v in nums:
                if v == 0:
                    result.append(all_multi)
                else:
                    cur = all_multi / v
                    result.append(int(cur))
        elif zero_count == 1:
            for v in nums:
                if v == 0:
                    result.append(all_multi)
                else:
                    result.append(0)

        if zero_count >= 2:
            return [0 for _ in range(len(nums))]
        
        return result


if __name__ == "__main__":
    solution = Solution()
    # nums = [1,2,3,4]
    # nums = [-1,1,0,-3,3]
    nums = [1,2,3,4,0,0]
    result = solution.productExceptSelf(nums)
    print(result)




