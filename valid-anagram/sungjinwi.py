'''
	풀이 :
		문자열 s에서 문자가 나올 때마다 딕셔너리에 저장하고 숫자 증가
        문자열 t에서 동일한 문자가 나올 때마다 숫자 감소시키고 0되면 딕셔너리에서 제거
        딕셔너리에 없는 문자가 나오거나 작업이 끝난 후 딕셔너리가 비어있지 않다면 False
        
	TC : 
		for문 두번 돌기 때문에 O(N)
        
    SC :
		딕셔너리 할당하는 메모리를 고려하면 O(N)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return (False)
        dic = {}
        for char in s :
            if char in dic :
                dic[char] += 1
            else :
                dic[char] = 1
        for char in t :
            if char in dic :
                dic[char] -= 1
                if dic[char] == 0 :
                    dic.pop(char)
            else :
                return (False)
        if dic :
            return (False)
        else :
            return (True)
