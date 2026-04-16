# TC : O(m^2 * n) m : len(strs), n : len(strs[0]) 
# SC : O(m * n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for str in strs:
            sorted_strs.append(sorted(str))
        
        answer = []
        
        i = 0

        visited = [False] * 10001

        while i < len(strs):
            if visited[i]:
                i = i + 1
                continue

            sub_answer = []
            target = sorted_strs[i]
            sub_answer.append(strs[i])

            for j in range(i+1, len(strs)):
                if sorted_strs[j] == target:
                    visited[j] = True
                    sub_answer.append(strs[j])
            
            i = i + 1
            answer.append(sub_answer)
        
        return answer
            
            
