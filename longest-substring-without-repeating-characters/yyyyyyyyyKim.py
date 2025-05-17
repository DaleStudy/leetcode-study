class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # 브루트포스(시간복잡도 : O(n^2))
        answer = 0

        for i in range(len(s)):
            # 중복없는 문자열을 저장할 집합
            substring = set()

            for j in range(i,len(s)):

                # 중복 문자를 만나면 break
                if s[j] in substring:
                    break

                # 중복 아니면 문자 추가하고 긴 문자열 길이 비교해서 업데이트
                substring.add(s[j])
                answer = max(answer, len(substring))

        return answer
