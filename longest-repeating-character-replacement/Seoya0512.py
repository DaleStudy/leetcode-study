
'''
2개의 포인터를 활용해 슬라이딩 윈도우 방식으로 문제를 해결
(접근법은 알고 있었지만 구현이 어려워 알고달레 참고)

참고
end-start+1-max(counter.values())는 윈도우를 전부 같은 문자로 만들기 위해 바꿔야 하는 최소 문자 수
즉, 그 값이 K개 이상 필요하면 유효하지 않은 것으로 판단함


Time Complexity: O(n)
- 문자열의 모든 문자를 한 번씩 방문
Space Complexity: O(1)
- 
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        counter = {}
        start = 0

        for end in range(len(s)):
            counter[s[end]] = counter.get(s[end], 0) + 1
            while end - start + 1 - max(counter.values()) > k:
                counter[s[start]] -= 1
                start +=1 
            max_len = max(end-start+1, max_len)
        
        return max_len 
