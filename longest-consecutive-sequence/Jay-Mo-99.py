# --- 해석 ---
#매개변수 nums 를 set으로 바꿔서 중복제거
#set을 list로 전환하여 sort하여 오름차순으로 변환
#for loop 로 nums[1]부터 nums[len(nums)-1] 에 접근
#nums[i]-nums[i-1] =1 이면 변수 current를 증가, longest는 current의 최댓값을 업데이트
#만약 해당 조건을 만족하지 않는다면 current를 1로 초기화, 이후 longest 값 return   
        
# --- Big O
#N: 매개변수 nums의 길이가 N이다. 
        
# Time Complexity: O(N)
#- set(nums)는 nums의모든 요소를 하나씩 순회하며 중복 제거 : O(N)
#- list(set(nums)) 는 data type을 변환하면서 nums의 갯수만큼 data를 추가 생성: O(N)
#- for loop 는 nums[1] 부터 nums[len(nums)-1]만큼 순회: O(N)
        
# Space Complexity: O(N)
#-nums = list(set(nums)): list(),set(),dict() 이런 data type을 변환할때마다 N만큼 공간 추가할당: O(N)
#-longest,current 변수는 상수 : O(1)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #If the nums doesn't have elements, return 0 
        if len(nums) ==0:
            return 0
        #중복제거 set 
        nums = list(set(nums))
        #sort 
        nums.sort()    
        print(nums)

        #Variables
        longest = 1
        current = 1

        #Approah all element of nums for checking the sequnece number or not
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                current +=1 #current는 nums[i]와 nums[i-1]의 차이가 1이면 +1해줌. 
                longest = max(longest, current) #return값을 위해 currrent가 가장 크도록 업데이트 
            else:#연속 되지 않을 시 current 1로 초기화
                current =1 
        print(longest)
        return longest


