class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(1)
    """
    def characterReplacement(self, s: str, k: int) -> int:      
        cnt_arr = [0] * 26
        max_cnt, max_len = 0, 0

        # Two pointers: left/right
        l = 0
        for r in range(len(s)):
            # Increase count and find max count by right pointer's alphabet
            idx = ord(s[r]) - ord("A")
            cnt_arr[idx] += 1
            max_cnt = max(max_cnt, cnt_arr[idx])
            
            # Left pointer moves if changable characters exceed k
            if (r - l + 1) - max_cnt > k:
                idx = ord(s[l]) - ord("A")
                cnt_arr[idx] -= 1
                l += 1
            
            # Update the max length
            max_len = max(max_len, r - l + 1)
        
        return max_len
            
tc = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4)
]

sol = Solution()
for i, (s, k, e) in enumerate(tc, 1):
    r = sol.characterReplacement(s, k)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
