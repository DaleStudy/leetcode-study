class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 슬라이딩 윈도우(시간복잡도 O(m+n), 공간복잡도 O(n) : m=len(s), n=len(t))
        # 필요한 문자 개수 딕셔너리로 정리
        need = {}
        for i in t:
            need[i] = need.get(i,0) + 1

        window = {}             # 현재 윈도우에 포함된 문자 개수 딕셔너리로 정리
        have = 0                # 조건을 만족한 문자 수
        need_count = len(need)  # 조건을 만족해야하는 문자 수
        min_len = 100001        # 최소윈도우길이(최대값을 초기값으로 설정)
        answer = ""
        left = 0

        # 오른쪽 포인터 이동
        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0) + 1

            # 해당 문자가 조건을 만족했다면 have += 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            
            # 모든 조건 만족하면 왼쪽 계속 줄이기
            while have == need_count:
                # 최소 윈도우 길이 갱신
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    answer = s[left:right+1]
                
                # 윈도우 왼쪽 문자 제거
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return answer
