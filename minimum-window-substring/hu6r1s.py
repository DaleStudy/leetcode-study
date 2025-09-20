class Solution:
    """
    접근 방법: https://www.youtube.com/watch?v=jSto0O4AJbM
        - t의 문자 개수를 미리 세어둔 후(t_count),
          s에서 두 포인터(left, right)를 이용해 슬라이딩 윈도우를 확장/축소하며
          모든 조건을 만족하는 최소 구간을 찾는다.
        - have: 현재 window에서 조건을 만족한 문자 종류 개수
        - need: t에 있는 문자 종류 개수
        - 조건을 만족할 때마다 왼쪽 포인터를 줄여 최소 길이 갱신

        시간복잡도:
        - 각 문자를 오른쪽 포인터로 한 번, 왼쪽 포인터로 한 번만 방문 → O(|s|)
        - t의 해시맵 구성 O(|t|)
        - 최종 시간복잡도 = O(|s| + |t|)

        공간복잡도:
        - window와 t_count 해시맵 → O(|s| + |t|)
    """
    def minWindow(self, s: str, t: str) -> str:
        t_count, window = {}, {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        have, need = 0, len(t_count)
        res, len_res = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in t_count and window[c] == t_count[c]:
                have += 1
            
            while have == need:
                if (right - left + 1) < len_res:
                    res = [left, right]
                    len_res = (right - left + 1)
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left:right+1] if len_res != float("infinity") else ""
