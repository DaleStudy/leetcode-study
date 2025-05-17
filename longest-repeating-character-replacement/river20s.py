class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(s)
        if n == 0:
            return 0

        left = 0
        max_len = 0
        char_counts = {} 
        max_freq_count = 0 

        for right in range(n):
            right_char = s[right]
            char_counts[right_char] = char_counts.get(right_char, 0) + 1
            max_freq_count = max(max_freq_count, char_counts[right_char])
            
            current_window_length = right - left + 1
            # 바꿔야 하는 문자 수 = 윈도우 길이 - 가장 많은 문자의 빈도수
            changes_needed = current_window_length - max_freq_count
            
            # 만약 바꿔야 하는 문자 수가 k보다 크면 윈도우를 줄여야 함
            if changes_needed > k:
                left_char = s[left]
                char_counts[left_char] -= 1
                if char_counts[left_char] == 0: 
                    del char_counts[left_char]
                left += 1

            max_len = max(max_len, right - left + 1) 

        return max_len
