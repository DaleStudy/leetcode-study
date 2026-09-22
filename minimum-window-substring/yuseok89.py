# TC: O(N)
# SC: O(N)
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        len_s = len(s)
        len_t = len(t)

        min_len = len_s + 1
        ans_start_idx = -1
        total_cnt = 0

        t_cnt_dict = Counter(t)
        cnt_dict = defaultdict(int)

        l, r = 0, 0

        while r < len_s:

            r_c = s[r]

            if cnt_dict[r_c] < t_cnt_dict.get(r_c, 0):
                total_cnt += 1

            cnt_dict[r_c] += 1
            r += 1

            while total_cnt == len_t:
                if min_len > r - l:
                    min_len = r - l
                    ans_start_idx = l

                l_c = s[l]

                if cnt_dict[l_c] <= t_cnt_dict[l_c]:
                    total_cnt -= 1

                cnt_dict[l_c] -= 1
                l += 1

        if ans_start_idx == -1:
            return ''

        return s[ans_start_idx:ans_start_idx + min_len]

