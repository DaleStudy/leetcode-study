# 시간 복잡도 : O(n), 공간 복잡도 : O(n)
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		tmp = {}
		# tmp에 char:횟수 형식으로 저장
		for key in s:
			if key in tmp:
				tmp[key] += 1
			else:
				tmp[key] = 1
		# t 문자열을 돌면서 나타나는 char에 대한 tmp의 횟수 차감
		# tmp에 존재하지 않는 char 발생 시 return False
		for key in t:
			if key in tmp:
				tmp[key] -= 1
			else:
				return False
		# tmp를 돌면서 value값이 모두 0인지 확인, 모두 0일 경우 s와 t는 anagram이다
		for i in tmp:
			if (tmp[i] != 0):
				return False
		return True

