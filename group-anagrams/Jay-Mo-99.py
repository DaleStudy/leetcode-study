﻿        #해석
        #tempDict = defaultdict(list) 로 자동으로 빈 리스트를 생성하는 딕셔너리
        #for loop 로 strs의 각 element를 순회
        #key=tuple(sorted(s)) 각 element인 s를 정렬하여 tuple로 변환하여 key로 저장한다 -> key는 변경 불가능 해야하므로 리스트 대신 tuple이 적합
        #tempDict[key].append(s) 로 key를 기준으로 element를 value값으로 tempDict에 저장한다. 
        #tempDict의 value값만 return하여 같은 key를 가지는 value가 list로 묶인 이중 list를 return한다. 

        #Big O
        #- N: strs 리스트의 element 갯수
        #- K: 각 element의 길이

        #Time Complexity: O(N∗K∗Log(K)) = O(N) * O(K*Log(K))
        #- sorted(s) : sort,sorted알고리즘은 Timsort 알고리즘이므로 정렬 대상 길이(K)에 영향받음 ->  O(K∗Log(K))
        #- for loop: strs의 element갯수만큼 순회 -> O(N)



        #Space Complexity: O(N∗K) = O(N) * O(N)
        #- tempDict key : 각 키는 최대 K 크기의 tuple로 저장 -> O(K)
        #- tempDict value: strs에 각 고유한 element만 있다면 tempDict의 value의 최댓값은 N개 -> O(N) 


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tempDict = defaultdict(list)
        
        for s in strs:
            key = tuple(sorted(s))
            tempDict[key].append(s)
        
        return list(tempDict.values())
        

