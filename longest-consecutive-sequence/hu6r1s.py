class Solution:
    """
        nums를 내림차순 sort하고, 차례대로 두 개의 차가 다음 차가 같다면 + 1
        처음 차는 diff 변수에 저장하고, 진행되면서 diff를 업데이트
        200, 100, 4, 3, 2, 1

        연속된 수열이라고 하여 1 이외의 다른 수가 올 수 있을 것이라고 판단하였지만 차이가 1로 나온다는 것을 확인

        - TC
            - set(nums) -> O(n)
            - for -> O(n)
            - while -> O(n)
            - 전체 -> O(n)
        - SC
            - num_set -> O(n)
            - 다른 변수들 -> O(1)
            - 전체 -> O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                k = 1
            
                while num + k in num_set:
                    k += 1
                
                longest = max(longest, k)
        return longest
