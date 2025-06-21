'''
문제의 의도
이 문제는 문자열 s에서 문자열 t의 모든 문자(중복 포함)를 포함하는 가장 짧은 부분 문자열을 찾는 문제임.

핵심 포인트:
1) t의 모든 문자가 포함되어야 함 (중복 개수도 맞아야 함)
2) 가장 짧은 길이의 부분 문자열을 찾아야 함
3) 연속된 부분 문자열이어야 함

해결 방법
슬라이딩 윈도우 + 투 포인터 기법을 사용함:
오른쪽 포인터로 윈도우를 확장하여 조건을 만족시킴
조건을 만족하면 왼쪽 포인터로 윈도우를 축소하여 최소 길이 찾기
해시맵으로 문자 개수를 효율적으로 관리

Example 1의 경우를 보면,

Input: s = "ADOBECODEBANC", t = "ABC"

실행 과정:
t_count: {'A':1, 'B':1, 'C':1}, required = 3
윈도우 확장: right 포인터로 "ADOBEC"까지 확장 → 조건 만족
윈도우 축소: left 포인터로 "ODEBANC" → "BANC"까지 축소
최종 결과: "BANC" (길이 4)

Output: "BANC"

시간 복잡도: O(|s| + |t|)
각 문자가 최대 2번 방문됨 (right 포인터로 1번, left 포인터로 1번)
t를 한 번 순회하여 해시맵 생성: O(|t|)
전체적으로 선형 시간 복잡도

공간 복잡도: O(|s| + |t|)
t_count 해시맵: O(|t|)
window_counts 해시맵: 최대 O(|s|)
기타 변수들: O(1)
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t가 빈 문자열이면 빈 문자열 반환
        if not t:
            return ""
        
        # t의 각 문자 개수를 저장하는 해시맵
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        # 조건을 만족하기 위해 필요한 고유 문자의 개수
        required = len(t_count)
        
        # 슬라이딩 윈도우의 왼쪽, 오른쪽 포인터와 조건을 만족하는 문자 개수 초기화
        left = 0
        right = 0
          
        # 현재 윈도우에서 조건을 만족하는 문자의 개수
        formed = 0
        
        # 현재 윈도우의 문자 개수를 저장하는 해시맵
        window_counts = {}
        
        # 결과를 저장할 변수들
        min_len = float('inf')
        min_left = 0
        min_right = 0
        
        # 오른쪽 포인터로 윈도우 확장
        while right < len(s):
            # 오른쪽 문자를 윈도우에 추가
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # 현재 문자의 개수가 t에서 요구하는 개수와 같아지면 formed에 1을 더함
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            # 모든 문자의 조건이 만족되면 왼쪽 포인터로 윈도우를 최소화 시도
            while left <= right and formed == required:
                char = s[left]
                
                # 현재 윈도우가 지금까지의 최소 길이보다 작으면 결과 업데이트
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                    min_right = right
                
                # 왼쪽 문자를 제거하고, 조건을 만족하지 않게 되면 formed에서 1을 뺌
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                # 왼쪽 포인터 이동
                left += 1
            
            # 오른쪽 포인터 이동
            right += 1
        
        # 결과 반환
        return "" if min_len == float('inf') else s[min_left:min_right + 1]



