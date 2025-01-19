# 문제유형 : Trie
class WordDictionary:
	def __init__(self):
		self.trie = {}

	# 시간 복잡도 : O(N)
	# 공간 복잡도 : O(N)
	def addWord(self, word: str) -> None:
		node = self.trie
		for char in word:
			if char not in node:
				node[char] = {}
			node = node[char]
		node['$'] = True

	# 시간 복잡도 : O(m^N) (m : 철자의 종류, N : 문자열의 길이)
	def search(self, word: str) -> bool:
		return self.dfs(0, self.trie, word)
	
	def dfs(self, i, node, word):
		if i == len(word):
			return '$' in node
		if word[i] == '.':
			for child in node.values():
				if isinstance(child, dict) and self.dfs(i + 1, child, word):
					return True
		if word[i] in node:
			return self.dfs(i + 1, node[word[i]], word)
		return False

