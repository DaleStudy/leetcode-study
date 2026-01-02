class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        # 결과를 저장할 변수 (최대 길이)
        max_length = 0
        
        # 윈도우 왼쪽 포인터
        left = 0
        
        # 현재 윈도우 내에서 가장 많이 등장한 문자의 빈도수
        max_frequency = 0
        
        # right 포인터를 0부터 끝까지 이동 
        for right in range(len(s)):
            current_char = s[right]
            
            # 현재 문자의 카운트 증가
            count[current_char] = count.get(current_char, 0) + 1
            
            # 현재 윈도우 내의 '최빈 문자' 개수 갱신
            # 새로 들어온 문자가 최빈 문자가 될 수도 있으므로 비교
            max_frequency = max(max_frequency, count[current_char])

            # 윈도우 크기 = (right - left + 1)
            # 나머지 문자 개수 = 윈도우 크기 - 최빈 문자 개수
            window_len = right - left + 1
            if (window_len - max_frequency) > k:
                # 왼쪽 문자를 윈도우에서 제거
                left_char = s[left]
                count[left_char] -= 1
                left += 1  # 왼쪽 포인터 이동
            max_length = max(max_length, right - left + 1)
            
        return max_length
