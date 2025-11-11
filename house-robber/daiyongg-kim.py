class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_prev_prev = 0
        rob_prev = 0
        max_today = 0
        for rob_current in nums:
            contains_rob_current = rob_current + rob_prev_prev
            not_contains_rob_current = rob_prev

            max_today = max(contains_rob_current, not_contains_rob_current)

            rob_prev_prev = rob_prev
            rob_prev = max_today
        
        return max_today
