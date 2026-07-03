class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_arr = []
        n = nums

        n.sort()

        for i in range(len(n) - 2):
            if n[i] > 0:
                break
            if i > 0 and n[i] == n[i - 1]:
                continue

            j = i + 1
            k = len(n) - 1
            while j < k:
                sum = n[i] + n[j] + n[k]

                if sum == 0:
                    result_arr.append([n[i], n[j], n[k]])
                    while j < k and n[j] == n[j + 1]:
                        j += 1
                    while j < k and n[k] == n[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1

        return result_arr
