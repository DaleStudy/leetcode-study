'''
문제의 의도
이 문제는 문자열에서 최대 k번의 문자 변경을 통해 같은 문자로만 이루어진 가장 긴 부분 문자열을 찾는 문제임.

핵심 포인트:
최대 k번까지 문자를 다른 문자로 바꿀 수 있음
바꾼 후 같은 문자로만 이루어진 부분 문자열의 최대 길이를 구해야 함
연속된 부분 문자열이어야 함

해결 방법
슬라이딩 윈도우(Sliding Window) + 해시맵 기법을 사용함:
윈도우 내에서 가장 빈도가 높은 문자를 찾기
나머지 문자들을 가장 빈도가 높은 문자로 바꾸는 데 필요한 변경 횟수 계산
변경 횟수가 k를 초과하면 윈도우 축소

실행 과정:
윈도우 "A": max_freq=1, 변경 필요=0 ≤ k=1 
윈도우 "AA": max_freq=2, 변경 필요=0 ≤ k=1 
윈도우 "AAB": max_freq=2, 변경 필요=1 ≤ k=1 
윈도우 "AABA": max_freq=3, 변경 필요=1 ≤ k=1 
윈도우 "AABAB": max_freq=3, 변경 필요=2 > k=1 
윈도우 축소: "ABAB" → max_freq=2, 변경 필요=2 > k=1 
계속 축소: "BAB" → max_freq=2, 변경 필요=1 ≤ k=1 
Output: 4 (윈도우 "AABA"에서 B 하나를 A로 바꾸면 "AAAA")

핵심 아이디어: 
윈도우 내에서 가장 많은 문자를 기준으로 하고, 
나머지 문자들을 그 문자로 바꾸는 데 필요한 변경 횟수가 k 이하인지 확인.

시간 복잡도: O(n)
각 문자가 최대 2번 방문됨 (right 포인터로 1번, left 포인터로 1번)
해시맵 연산은 O(1)이므로 전체적으로 선형 시간

공간 복잡도: O(1)
영어 대문자만 사용하므로 해시맵 크기는 최대 26개로 상수
기타 변수들도 상수 공간
'''
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 현재 윈도우 내 각 문자의 개수를 저장하는 해시맵
        char_count = {}
        
        # 슬라이딩 윈도우의 시작점
        left = 0
        
        # 윈도우 내에서 가장 빈도가 높은 문자의 개수
        max_freq = 0
        
        # 결과로 반환할 최대 길이
        max_length = 0
        
        # 오른쪽 포인터로 문자열을 순회하며 윈도우 확장
        for right in range(len(s)):
            # 현재 문자를 윈도우에 추가하고 빈도 증가
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1
            
            # 현재 윈도우에서 가장 빈도가 높은 문자의 개수 업데이트
            max_freq = max(max_freq, char_count[char])
            
            # 현재 윈도우 크기
            window_size = right - left + 1
            
            # 변경해야 할 문자 개수 = 전체 윈도우 크기 - 가장 많은 문자 개수
            # 이 값이 k보다 크면 윈도우가 유효하지 않음
            if window_size - max_freq > k:
                # 왼쪽 문자를 윈도우에서 제거하고 왼쪽 포인터 이동
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
            
            # 현재 윈도우 크기로 최대 길이 업데이트
            max_length = max(max_length, right - left + 1)
        
        return max_length




