# O(N^3) times, O(1) spaces
# 내부 while문의 관계가 외부 while문의 sub_str_len에 따라 반복횟수가 줄어드므로, 1+2+...N = N(N-1)/2 = O(N2) 시간 소요
# 추라고 내부 while에서 sub_str_len에 따라 s가 인덱싱되므로 최대 O(N) 시간이 소요
# 최종적으로 O(N^2 * N) = O(N^3)이 소요됨
class Solution:
    def countSubstrings(self, s: str) -> int:
        sub_str_len = 1
        result = 0

        while sub_str_len <= len(s):
            start_idx = 0
            while start_idx + sub_str_len <= len(s):
                sub_str = s[start_idx:start_idx+sub_str_len]
                if sub_str == sub_str[::-1]:
                    result += 1
                start_idx += 1

            sub_str_len += 1
        

        return result

# DP 풀이
# O(N^2) times, O(N^2) spaces
# start, end 지점을 순회하면서 이전 계산값을 재사용하여 회문을 파악
class Solution2:
    def countSubstrings(self, s: str) -> int:
        dp = {}

        for end in range(len(s)):
            for start in range(end, -1, -1):
                if start == end:
                    dp[(start, end)] = True
                elif start + 1 == end:
                    dp[(start, end)] = s[start] == s[end]
                else:
                    dp[(start, end)] = s[start] == s[end] and dp[(start+1, end-1)]

        return list(dp.values()).count(True)
