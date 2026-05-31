from collections import defaultdict


# 7기 풀이
# 시간 복잡도: O(n)
# - s의 길이(n)만큼의 시간복잡도
# 공간 복잡도: O(1)
# - char_dict에는 최대 26개의 알파벳만큼 저장 + 몇 개의 변수
class Solution:
    # 윈도우가 늘어나는 조건(right가 올라가는 조건): t의 알파벳 전체가 윈도우에 모두 포함될 때까지
    # 윈도우가 유지되는 조건(left가 올라가는 조건): t의 알파벳 전체가 윈도우에 포함이 된 후, 한 개라도 누락될 때까지
    def minWindow(self, s: str, t: str) -> str:
        char_dict = defaultdict(int)

        # t의 구성 알파벳 정보 저장
        for tt in t:
            # 알파벳 당 몇 개가 있는지 char_dict에 저장
            char_dict[tt] += 1
        # t에 있는 알파벳 종류의 개수
        need_alpha = len(char_dict)

        left = 0
        res = ""

        for right in range(len(s)):
            if s[right] in char_dict:
                # s[right]가 char_dict에 있다면 윈도우에 해당 알파벳이 있다는 의미로
                # char_dict에서 하나 차감
                char_dict[s[right]] -= 1
                if char_dict[s[right]] == 0:
                    # 해당 알파벳의 개수가 0이 되면 필요한 알파벳 중 하나를 다 찾았으므로
                    # need_alpha를 하나 차감
                    need_alpha -= 1

            while need_alpha == 0:
                # need_alpha가 0이라는 의미는 모든 글자를 다 찾았다는 의미
                # 윈도우를 유지하며 left를 올린다
                if not res or right - left + 1 < len(res):
                    # 현재의 res 글자보다 left / right 간 사이가 작을 때 res 업데이트
                    res = s[left:right + 1]
                if s[left] in char_dict:
                    # s[left]가 char_dict에 있다는 것은 left를 옮길 때 해당 알파벳은 누락이 되기 때문에
                    # 다음 윈도우 구간에서는 다시 필요하므로 char_dict 내 해당 알파벳 개수를 다시 증가
                    # need_alpha도 하나 증가 시켜줘야 한다.
                    if char_dict[s[left]] == 0:
                        need_alpha += 1
                    char_dict[s[left]] += 1
                
                # left 이동
                left += 1

        return res
