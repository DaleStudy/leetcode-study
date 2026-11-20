# Two pointer 최종 풀이
#Time: O(n^2) Space:O(n)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer=set()
        nums.sort()
        k=len(nums)
        for i in range(k-2):
            if nums[i] > 0: #nums를 정렬했기 때문에 이후에 합이 0이 되는 것은 불가능
                break
            if i== 0 or nums[i] != nums[i - 1]:  #인접한 값이 서로 다를 때만, i=0일때는 인덱스가 -1, 즉 마지막 원소와 비교하지 않고 바로 loop
                left,right=i+1,k-1
                while left<right: #left 와 right의 인덱스가 같아지기 전까지 
                    sum_val=nums[i]+nums[left]+nums[right]
                    if sum_val==0:
                        answer.add(tuple((nums[i],nums[left],nums[right])))
                        left+=1
                        right-=1
                    elif sum_val<0:
                        left+=1
                    else:
                        right-=1
        return list(answer)




# 2번째
#Time: O(n^2), Space: O(n)
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         answer=set()
#         nums.sort()
#         k=len(nums)
#         for i in range(k-2):
#             if nums[i]>0: 
#                 break #nums[i] > 0이면 이후 합이 0이 될 수 없어 종료
#             if i > 0 and nums[i] == nums[i-1]: #중복 제거
#                 continue 
#             candid=set() #target이 candid안에 있으면 세 수의 합이 "0"
#             for j in range(i+1,k): #i를 고정
#                 target=-(nums[i]+nums[j])
#                 if target not in candid:
#                     candid.add(nums[j])
#                 else:
#                     answer.add(tuple((nums[i],nums[j],target)))
#         return list(answer)



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
        
