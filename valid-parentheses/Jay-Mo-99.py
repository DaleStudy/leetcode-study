﻿        #해석
        #매개변수 string s의 각 character인 c 가 open bracket이면 temp 리스트에 추가한다. 
        #c가 close bracket이면 temp의 마지막 element와 짝이 맞는지 검사한다. 짝이 아니거나 temp에 아무 요소도 없으면 return false
        #검사 이후 temp에 잔여 요소가 남아있으면 짝이 맞지 않았다는 뜻이니 return false, 아닐 경우 return true

        #Big O
        #- N: 문자열 s의 길이

        #Time Complexity: O(N) = O(N) + O(1)
        #- for c in s : string s의 character의 수 만큼 진행된다. -> O(N)
        #-temp.append(c), temp.pop() : 리스트 연산은 상수 취급 -> O(1)

        #Space Complexity: O(N)
        #- temp : list temp은 최대 string s의 character수 만큼 요소를 저장할 가능성이 있다. 


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        for c in s:
            #If c is Open bracket, append to the list
            if (c == "(") or (c=="{") or (c=="["):
                temp.append(c)
            #If C is Close bracket, Check the close bracket pairs with last elememt of temp list 
            else:
                #There's no element in the tmep, Return false
                if(len(temp)==0):
                    return False
                
                if(c==")") and (temp.pop()=="("):
                    continue
                if(c=="}") and (temp.pop()=="{"):
                    continue
                if(c=="]") and (temp.pop()=="["):
                    continue
                else:
                    return False

        #After loop, Check temp is empty or not. 
        #If all c of s is pairs each other, the temp list is empty. 
        if (len(temp) == 0) :
            return True
        else:
            return False
        







