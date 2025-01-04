        #해석
        #문자열 s의 재배치로 문자열 t를 구성할 수 있으면 anagram으로 return true. 
        #s와 t를 list로 바꾸고 sort하여 오름차순으로 정렬시킨다, 둘이 같으면 같은 문자를 가진 문자열 리스트이므로 return true 
        
        #Big O
        #N: 주어진 문자열 s와 t의 길이(N)
        
        #Time Complexity: O(N)
        #- 문자열을 list로 변환하는 작업: O(N)
        #- 정렬작업 : NO(log N)
        #- 리스트 비교 작업, s와 t의 각 문자가 서로 일치하는지 체크한다 : O(N)
        #- 최종: O(N)
        
        #Space Complexity: O(N)
        #- list s와 t는 주어진 문자열 s와 t에 기반하여 새로운 list 객체로 할당된다: O(N)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s) #Convert string to list
        t = list(t)
        s.sort()    #Sort the list 
        t.sort()

        return s == t #If the s and t are same, return true(anagram)
        


