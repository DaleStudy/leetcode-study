﻿        #해석
        #encode함수: 매개변수 strs 리스트를 join 메소드와 특정 매개변수를 사용해 하나의 string인 answer로 전환
        #decode함수: 매개변수 string s를 split 메소드를 사용해 특정 매개변수를 기점으로 나누어 list로 전환하여 return한다. 
        #           만약 strs가 비어있을때는 특정 string을 주입하여 decode 에서 해당 string을 인식하여 빈 배열([])를 return한다. 


        #Big O
        #N: 리스트 strs의 길이 (element 갯수)
        #L: strs의 각 element 평균 길이 (문자열의 길이) 
        #M: string s 의 길이 

        #Time Complexity: 
        #-encode: O(N*L)
        #-- join(strs): 리스트에 있는 N개의 element와 각 문자열의 길이 L을 합산하여 문자열 생성 -> O(N * L)
        #-decode: O(M):
        #- split('구분자'): split 메서드는 구분자를 찾는 과정에서 string s를 순회하므로 -> O(M)



        #Space Complexity:
        #-encode: O(N*L)
        #-- answer: join 메서드로 생성되는 문자열은 strs 리스트의 모든 문자열을 합친 값이므로 -> O(N * L)
        #-decode: O(M)
        #-- answer:split 메서드로 생성되는 리스트는 string s의 길이에 비례하여 메모리를 차지 -> O(M)
        


class Solution:


    def encode(self, strs: List[str]) -> str:
        answer = '!@#$%123456789'.join(strs)
        if len(strs) == 0:
            answer = "I am empty"
        return answer

    def decode(self, s: str) -> List[str]:
        answer = s.split('!@#$%123456789')
        if s == "I am empty":
            answer = []
        return answer
    


