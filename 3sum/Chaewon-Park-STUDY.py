#Time: O(n^2), Space: O(n)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer=set()
        nums.sort()
        k=len(nums)
        for i in range(k-2):
            if nums[i]>0: 
                break #nums[i] > 0이면 이후 합이 0이 될 수 없어 종료
            if i > 0 and nums[i] == nums[i-1]: #중복 제거
                continue 
            candid=set() #target이 candid안에 있으면 세 수의 합이 "0"
            for j in range(i+1,k): #i를 고정
                target=-(nums[i]+nums[j])
                if target not in candid:
                    candid.add(nums[j])
                else:
                    answer.add(tuple((nums[i],nums[j],target)))
        return list(answer)



# 첫번째 풀이: TLE 
# brute force 방식
# 재귀  및 백트래킹 nums를 오름차순으로 정렬한 이유는 tuple은 (-1,-1,2) (2,-1,-1) 서로 다른 쌍으로 봐서
#Time:O(n^3) Space:O(n)

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         answer=set()
#         k=len(nums)
#         nums.sort()

#         arr=[]

#         def dfs(start):
#             if len(arr)==3:
#                 if sum(arr)==0:
#                     answer.add(tuple(arr))
#                     return 
#                 return 
#             for i in range(start,k):
#                 arr.append(nums[i])
#                 dfs(i+1)
#                 arr.pop()
#         dfs(0)
#         return list(answer)


        
