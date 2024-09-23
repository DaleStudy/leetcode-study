class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(N)
    # set에서 제외하는 로직을 없애기 위해, map을 사용해서 idx값을 저장후, start와 비교해서 start보다 작은 idx를 가진 경우에는 중복이 아니라고 판단했습니다.
    def lengthOfLongestSubstring(self, s: str) -> int:

        last_idx = {}
        answer = 0
        start = 0

        for idx, ch in enumerate(s):
            # 중복 조회시 idx값과 start 값 비교를 통해, 삭제하는 로직을 없이 중복을 확인했습니다.
            if ch in last_idx and last_idx[ch] >= start:
                start = last_idx[ch] + 1
                last_idx[ch] = idx
            else:
                answer = max(answer, idx - start + 1)
                last_idx[ch] = idx

        return answer
