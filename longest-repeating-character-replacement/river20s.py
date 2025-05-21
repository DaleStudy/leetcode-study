class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(s)

        if n == 0: 
            return 0

        left = 0            # 윈도우의 왼쪽 인덱스 (시작)
        max_len = 0         # 가장 긴 유효한 부분 문자열 길이
        char_counts = {}    # 현 윈도우 안에서 각 문자 빈도수
        max_freq_count = 0  # 현 윈도우 안에서 가장 많이 등장한 문자 빈도수

        for right in range(n):
            right_char = s[right] # 윈도우 오른쪽에 추가할 문자

            # 추가할 문자 빈도수 갱신
            char_counts[right_char] = char_counts.get(right_char, 0) + 1

            max_freq_count = max(max_freq_count, char_counts[right_char])
            
            current_window_length = right - left + 1

            # 바꿔야 하는 문자 수 = 윈도우 길이 - 가장 많은 문자의 빈도수
            changes_needed = current_window_length - max_freq_count
            
            # 만약 바꿔야 하는 문자 수가 k보다 크면 
            # 유효하지 않은 윈도우 => 윈도우를 줄여야 함
            if changes_needed > k:
                left_char = s[left] # 제거할 문자
                char_counts[left_char] -= 1 # 빈도수 줄이기

                left += 1 # 윈도우 축소

            # 최대 길이 업데이트, 반환
            max_len = max(max_len, right - left + 1) 

        return max_len
