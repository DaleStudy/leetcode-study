# 시간복잡도 : O(n*mlogm) (n은 strs의 길이, m은 strs의 원소의 길이)
# 공간복잡도 : O(n)

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		anagrams = collections.defaultdict(list)
		for word in strs:
			anagrams[''.join(sorted(word))].append(word)
		return list(anagrams.values())
	
