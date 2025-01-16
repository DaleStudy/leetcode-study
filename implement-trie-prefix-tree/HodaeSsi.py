# 시간복잡도: O(n) (n은 문자열의 길이)
# 공간복잡도: O(n) (n은 문자열의 길이)
class Trie:
	def __init__(self):
		self.root = {}
		self.end = False

	def insert(self, word: str) -> None:
		node = self.root
		for char in word:
			if char not in node:
				node[char] = {}
			node = node[char]
		node[self.end] = True
	
	def search(self, word: str) -> bool:
		node = self.root
		for char in word:
			if char not in node:
				return False
			node = node[char]
		return self.end in node
	
	def startsWith(self, prefix: str) -> bool:
		node = self.root
		for char in prefix:
			if char not in node:
				return False
			node = node[char]
		return True

