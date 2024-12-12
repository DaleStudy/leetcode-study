class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #해석
        #sets는 복수 요소를 허용하지 않는다(sets don't allow duplicate elements.)
        #만약 set에 기반된 list가 기존 nums와 길이가 다르다면 duplicate element가 있었다는 뜻이다. 
        #If the length of the set created from nums is different from the original list(nums), It means there are duplicates. 
        
        #Big O
        #N: 주어진 배열 nums의 길이(Length of the input list nums)
        
        #Time Complexity: O(N)
        #- set은 nums의 길이 n에 기반하여 생성된다(Creating a set from nums): O(N)
        #- 생성된 list와 기존 nums와의 비교는 상수(Comparing the lengths between created list and original list) : O(1)
        
        #Space Complexity: O(N)
        #-set은 nums의 길이에 의해 생성되므로 n에 영향받음(The set requires extra space depends on the size of nums) : O(N) 
        if len(list(set(nums))) == len(nums): 
            return False
        else:
            return True
