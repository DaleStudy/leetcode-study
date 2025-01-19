class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        딕셔너리를 사용하여 이전에 나왔던 인덱스를 기억
        중복되지 않았다면 answer를 저장해 나감
        중복이 발생하고 begin과 end사이라면 중복 발생 원인 다음을 begin으로 세팅 후 다시 계산

        Time Complexity : O(n)
        Space Complexity : O(n)

        """ 
        answer, begin, end = 0, 0, 0
        hash_map = dict()

        while end < len(s):
            ch = s[end]
            hash_map[ch] = hash_map.get(ch, -1)

            if hash_map[ch] == -1: #한 번도 나오지 않았다.
                hash_map[ch] = end
                answer = max(answer, end-begin+1)
            else:
                if begin<=hash_map[ch]<end: #중복이 생겼다.
                    begin = hash_map[ch]+1
                else:
                    answer = max(answer, end-begin+1)
                hash_map[ch] = end
            end += 1
        
        return answer

