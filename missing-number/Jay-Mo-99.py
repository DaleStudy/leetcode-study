        #해석
        #nums가 0에서 len(nums) 까지의 숫자를 포함하나 확인하고, 없다면 해당 숫자를 return한다. 
        #nums를 오름차순 정렬한다 
        #nums가 조건을 만족하면, nums[i]는 인덱스 i와 동일해야한다. (e.g nums[0] =0, nums[1]=1)
        #배열의 마지막 요소(nums(len(num-1))) 이 len(nums)와 동일하지 않으면 nums은 0~len(nums) 까지의 숫자를 가진다는 조건을 만족 X -> 누락된 len(nums)를 return한다.
        #for loop 로 각 숫자가 인덱스와 일치 여부 확인
        #인덱스와 값이 일치하지 않는 nums[i]의 인덱스를 return한다.


        #Big O
        #N: 매개변수 n의 크기(계단 갯수)
        
        #Time Complexity: O(nlog(n)) = O(nlog(n))+O(1)+O(n)
        #- n: nums배열의 길이 
        #- sort(): Timsort방식이기에 O(nlog(n))
        #-if(nums[len(nums)-1] != len(nums)): 단일 조건 비교는 O(1)
        #for loop: nums의 길이에 비례하므로 O(n)

        
        #Space Complexity: O(1)
        #- sort(): nums.sort()는 제자리 정렬이기에 추가 공간 필요치 않으므로 O(1)

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the list 
        nums.sort()
        # If the last element of nums doesn't align with the numbers of element in nums, return len(nums)
        # For example, nums[0,1] so range is [0:2] but there's no last element of 2 so return 2(len(nums))
        if(nums[len(nums)-1] != len(nums)):
            return len(nums)
        #If each element doesn't match with the number of [0:len(nums)], return the i(index)
        for i in range(len(nums)):
            if nums[i] != i:
                print(nums[i],i)
                return i
            


