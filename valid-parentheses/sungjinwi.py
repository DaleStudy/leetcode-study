"""
	풀이 :
		stack구조를 이용해서 구현
		괄호의 페어를 딕셔너리의 key, value를 이용해 매치시킨다
		여는 괄호를 만나면 stack에 push, 닫는 괄호를 만나면 stack의 마지막 괄호의 pair일 때 pop, 아니면 return False
		문자열 전체를 순회했을 때 stack에 남아있으면 안 닫힌 괄호가 있으므로 return False

	s의 길이 N

	TC : O(N)
		s에 대해 한번 for문
	SC : O(N)
		stack의 최대 크기는 s의 길이와 비례
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = dict(zip('({[',')}]'))
        for paren in s :
            if paren in pair :
                stack.append(paren)
            elif not stack :
                return False
            elif pair[stack.pop()] != paren :
                return False
        if not stack :
            return True
        else :
            return False
