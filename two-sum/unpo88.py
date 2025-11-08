class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            diff = target - num

            if diff in num_to_index:
                j = num_to_index[diff]   
                return [i, j]
            
            num_to_index[num] = i

""" 
================================================================================
풀이 과정
================================================================================

[1차 시도] Brute Force - O(n^2)
────────────────────────────────────────────────────────────────────────────────
1. 단순 반복으로 그냥 문제를 풀어보자.
2. 단 같은 숫자일 경우에는 넘어가자.

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

3. O(n^2) 으로 문제를 풀었는데
4. 시간이 오래걸리니까 다른 풀이 방법이 있는 것 같음


[2차 시도] Hash Table - Two Pass
────────────────────────────────────────────────────────────────────────────────
5. 해싱으로 문제를 풀 방법이 있으려나?
6. 넘버마다 인덱스를 저장하고
7. target에서 현재 가진 값을 뺀 값이 nums에 있는지를 판단하면 될 것 같은데?
8. 그리고 현재 가진 값과 뺀 값의 인덱스를 그대로 반환하면 될 것 같고
9. 근데 동일한 인덱스는 제외해야할듯

        num_index_dict = defaultdict()
        for index, num in enumerate(nums):
            num_index_dict[num]=index
        print(num_index_dict)

        for index, num in enumerate(nums):
            if (target - num) in nums and num_index_dict[target - num] != index:
                return [index, num_index_dict[target-num]]


[3차 시도] Hash Table - One Pass  
────────────────────────────────────────────────────────────────────────────────
10. 단 한 번의 루프에서도 동작시킬 수 있을듯?

        num_index_dict = defaultdict()

        for index, num in enumerate(nums):
            if (target - num) in num_index_dict:
                return [index, num_index_dict[target - num]]

            num_index_dict[num] = index


[최종 개선] 코드 가독성 향상
────────────────────────────────────────────────────────────────────────────────
11. 속도가 많이 빨라졌다. 코드 가독성만 높여보자

        num_to_index = {}
        
        for i, num in enumerate(nums):
            diff = target - num

            if diff in num_to_index:
                j = num_to_index[diff]   
                return [i, j]
            
            num_to_index[num] = i
"""
