"""
	sliding window 풀이:
		알고달레 풀이 참조할 것
		start부터 end까지의 부분문자열 길이가 유기적으로 변하면서 이동하여 탐색
		s[end]가 set에 존재하지 않으면 s[end] set에 추가하고 ans와 대소비교로 업데이트, end + 1 -> 부분문자열 크기 증가
		s[end]가 set에 존재하면 s[start] set에서 제거하고 start + 1 -> s[end]와 같은 문자가 set에 없을 때까지 부분문자열 크기 감소
	
	TC : O(N)
		문자열 한번만 순회하고 set의 조회, 추가, 삭제는 O(1)이므로
	SC : O(N)
        문자열 길이와 set의 크기가 비례
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start, end = 0, 0
        chars = set()
        while end < len(s) :
            if not s[end] in chars :
                chars.add(s[end])
                ans = max(ans, end - start + 1)
                end += 1
            else :
                chars.remove(s[start])
                start += 1
        return ans

"""
	기존 풀이 : 
		각 문자를 start로 순회하는 내부에서 
		새로 추가되는 end 문자와 기존 문자열을 중복검사해서 길이를 늘려나가다가 중복되면 break

	TC : O(N^2)
	SC : O(N)

	class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        dp = [1] * len(s)
        for start in range(len(s)):
            chars = set()
            for end in range(start, len(s)) :
                if not s[end] in chars :
                    chars.add(s[end])
                    ans = max(ans, end - start + 1)
                else :
                    break
        return ans
"""
