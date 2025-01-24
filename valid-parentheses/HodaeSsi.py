# 시간 복잡도 : O(n)
# 공간 복잡도 : O(n)
# 문제 유형 : Stack
class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		
		for char in s:
			if char in (')', '}', ']'):
				if not stack or stack.pop() != {')': '(', '}': '{', ']': '['}[char]:
					return False
			else:
				stack.append(char)
	
		return not stack
	
