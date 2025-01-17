# 시간복잡도: O(n)
# 공간복잡도: O(1)

class Solution:
	"""
	@param: strs: a list of strings
	@return: encodes a list of strings to a single string.
	"""
	def encode(self, strs):
		if not strs:
			return ""
		return chr(257).join(strs)

	"""
	@param: str: A string
	@return: decodes a single string to a list of strings
	"""
	def decode(self, str):
		if not str:
			return []
		return str.split(chr(257))
	
