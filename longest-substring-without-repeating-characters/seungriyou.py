# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring_slow(self, s: str) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            two pointer를 이동해가며 substring을 확인하는 과정에서, hash table을 이용하여 duplicate character를 O(1)에 lookup 할 수 있도록 한다.
            p1, p2를 각각 왼쪽과 오른쪽 pointer라고 할 때,
                - substring의 맨 오른쪽 문자가 duplicate이 아니면, seen에 추가하고 맨 오른쪽 범위를 한 칸 늘린다. 그리고 max_len을 업데이트 한다.
                - substring의 맨 오른쪽 문자가 duplicate이면, seen에서 맨 왼쪽 문자를 삭제하고 맨 왼쪽 범위를 한 칸 줄인다.
        """

        p1 = p2 = max_len = 0
        seen = set()

        while p2 < len(s):
            # p2가 중복이 아닌 문자를 가리키면, seen에 추가하고 p2 한 칸 옮기기
            if s[p2] not in seen:
                seen.add(s[p2])
                p2 += 1
                # max_len 업데이트
                max_len = max(max_len, p2 - p1)

            # p2가 중복인 문자를 가리키면, seen에서 s[p1] 삭제하고 p1 한 칸 옮기기
            else:
                seen.remove(s[p1])
                p1 += 1

        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            lengthOfLongestSubstring_slow()의 경우, p2가 중복인 문자를 가리킬 때 p1을 한 칸씩만 이동한다.
            하지만 해당 문자가 가장 마지막으로 나온 인덱스를 기록해둔다면, 바로 그 다음 인덱스로 p1을 이동시킬 수 있다.
            이러한 인덱스를 lookup 하는 행위도 hash table을 이용해 O(1)으로 최적화 할 수 있다.
        """

        p1 = max_len = 0
        seen = dict()

        for p2, right in enumerate(s):
            # right 문자가 p1 ~ p2 내 범위에서 이미 등장했다면, p1을 right 문자가 가장 마지막으로 등장한 인덱스의 다음 위치로 이동
            if seen.get(right, -1) >= p1:
                p1 = seen[right] + 1

            # 그렇지 않다면, p1을 그대로 두고 max_len 업데이트
            else:
                max_len = max(max_len, p2 - p1 + 1)

            # right를 seen에 기록
            seen[right] = p2

        return max_len
