# 시간복잡도 O(n^2), 공간복잡도 O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # key: 값, value: list((i, j))
        dic = {}
        answer = set()

        # 이중 for문으로 모든 경우의 수를 구합니다.
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] in dic:
                    dic[nums[i] + nums[j]].append((i, j))
                else:
                    dic[nums[i] + nums[j]] = [(i, j)]

        for k in range(len(nums)):
            for i, j in dic.get(-nums[k], []):
                if i != k and j != k:
                    answer.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return list(answer)
   
