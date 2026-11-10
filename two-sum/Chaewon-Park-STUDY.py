class Solution:
    #시간, 공간 복잡도:O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr={} #elem를 key로 바로 저장하여 시간복잡도 O(1)
        for i, elem in enumerate(nums): 
            if target -elem in arr: #왜 arr에서 찾는지 nums에서 찾으면 리스트라서 역시 복잡도 올라감
            # 두 수의 합이므로 나머지 짝이 arr에 있는지 확인
                return [arr[target - elem], i]
            arr[elem] = i #없으면 arr에 저장




# 처음 시도 풀이 DFS(기각, runtime: 7013ms)
# 시간 복잡도: O(n^2), 공간 복잡도: O(1)

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         arr = []

#         def dfs(start):
#             if len(arr) == 2:
#                 return nums[arr[0]] + nums[arr[1]] == target  #정답 발견시 True반환
#             for i in range(start, len(nums)):
#                 arr.append(i)
#                 if dfs(i + 1):  # 정답이면 True를 위로 전달해 탐색 종료
#                     return True
#                 arr.pop()
#             return False

#         dfs(0)
#         return arr
