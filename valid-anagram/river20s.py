class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        s와 t의 길이가 같다는 전제 아래
        s와 t를 각각 딕셔너리에 저장하고
        딕셔너리끼리 비교하여 애너그램 여부를 검사하는 함수.

        - 시간 복잡도: O(n)
        - 공간 복잡도: O(n)
          알파벳 소문자로 한정할 경우 O(1)로 볼 수도 있지만
          추가 사항인 UNICODE 문자가 입력될 경우를 고려하여
          공간 복잡도를 O(n)으로 계산함. 
          
        """
        # 먼저 s와 t의 길이 비교
        # s와 t가 애너그램이라면 길이가 같음
        if len(s) != len(t):
            return False
        
        # 입력 받은 s의 각 문자를 키, 빈도를 값으로 하는 딕셔너리 
        sdict = {}

        # s의 각 문자를 순회하면서 sdict 구축
        # O(n) 시간 소요

        for char in s:
            if char in sdict:
                sdict[char] += 1
            else:
                sdict[char] = 1
        
        # 입력 받은 t의 각 문자를 키, 빈도를 값으로 하는 딕셔너리
        tdict = {}

        # t의 각 문자를 순회하면서 tdict 구축
        # O(n) 시간 소요

        for char in t:
            if char in tdict:
                tdict[char] += 1
            else:
                tdict[char] = 1
        
        # Python은 키의 순서에 상관 없이 딕셔너리끼리 바로 비교 가능
        # sdict와 tdict 비교 후 같으면 True 같지 않으면 False 반환
        # 딕셔너리 안의 키의 수가 k이고 모든 문자가 개별적이라면,
        # 시간은 O(k)가 필요
        # 여기서 k는 O(n) 수준이므로 전체 시간 복잡도는 O(n)
         
        if sdict == tdict:
            return True
        else:
            return False
