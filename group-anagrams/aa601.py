#시간복잡도 O(n * klogk)
#공간복잡도 O(n * k)
#			=> n개의 단어 * 각 단어의 k만큼의 길이
class Solution:
	def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		ans = {}

		for word in strs:
			# 단어의 문자를 정렬 후 키로 사용
			sortedWord = ''.join(sorted(word)) # sorted()의 시간복잡도 : O(klogk)
			# 초기 리스트 생성
			if sortedWord not in ans:
				ans[sortedWord] = []
			ans[sortedWord].append(word)

		# 딕셔너리의 value를 list로 변환
		ansLst = list(ans.values())
		return ansLst
	
