class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = {}
        for word in strs:
            key = "".join(sorted(word))
    # key가 seen에 이미 있으면 → word 추가
    # 없으면 → 새로 만들기
            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word] 
        return list(seen.values())

