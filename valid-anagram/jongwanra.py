"""
[Problem]
https://leetcode.com/problems/valid-anagram/

[Brain Storm]
아나그램인 경우, true, 아니면 false 반환
동일한 알파벳이 중복되어 사용될 수 있다.

[Plan]
1. s에 대해 for-loop을 순회하며 alphabet-count 형태로 map을 만든다.
2. t에 대해 for-loop을 순회한다.
    2-1. t의 alphabet이 alphabet-count > 0 인 경우, count -= 1을 한다.
    2-2. 없는 경우, false로 return 한다.
3. alphabet-count 가 빈 경우 true 그렇지 않으면 false를 반환한다.

[Complexity]
t.length = N
s.length = M

Time: O(N + M)
Space: O(M)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet_to_count = {}
        for alphabet in s:
            alphabet_to_count[alphabet] = alphabet_to_count.get(alphabet, 0) + 1

        for alphabet in t:
            count = alphabet_to_count.get(alphabet, -1)
            if count == -1:
                return False

            count -= 1
            if count == 0:
                alphabet_to_count.pop(alphabet)
            else:
                alphabet_to_count[alphabet] = count

        return len(alphabet_to_count) == 0



sol = Solution()
# Normal Case
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))

