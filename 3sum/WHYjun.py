class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        sortedNums = sorted(nums)

        for i in range(len(sortedNums)):
            # skip if same to avoid dup
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue

            # use two pointers
            j = i + 1
            k = len(sortedNums) - 1

            while j < k:
                total = sortedNums[i] + sortedNums[j] + sortedNums[k]

                if total == 0:
                    answer.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    j += 1
                    # skip if same to avoid dup
                    while sortedNums[j] == sortedNums[j-1] and j < k:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return answer
        