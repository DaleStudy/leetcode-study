"""
    풀이 : 슬라이딩 윈도우 이용
        딕셔너리를 이용해 문자의 등장 빈도를 확인, 증가, 감소시킨다
        t에 존재하는 모든 문자의 빈도보다 s의 빈도가 같거나 커질 때까지 right를 증가시킨다
        left를 증가시키며 s[left]의 문자빈도가 t보다 낮아지는 지점을 찾는다
        기존의 min_total길이보다 짧으면 ans에 left, right 정보를 이용해 update
    
    알고달레 참조 및 좀 더 최적화 필요

    s의 길이 : n

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        min_total = len(s)
        s_appear = {}
        t_appear = {}
        ans = ""
        for char in set(t):
            s_appear[char] = 0
            t_appear[char] = t.count(char)
        while (right < len(s)):
            if s[right] in s_appear:
                s_appear[s[right]] += 1
            if all(s_appear[char] >= t_appear[char] for char in t_appear.keys()):
                while left < right:
                    if s[left] in s_appear:
                        if s_appear[s[left]] == t_appear[s[left]]:
                            break
                        s_appear[s[left]] -= 1
                    left += 1
                if (right - left + 1) < min_total:
                    min_total = right - left + 2
                    ans = s[left:right + 1]
            right += 1
        return ans
