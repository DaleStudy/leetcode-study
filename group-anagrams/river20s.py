import collections
from typing import List

class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        각 문자열을 순회하면서 알파벳 순으로 정렬한 결과를 tuple로 변환하여 Key로 하고,
        그 Key의 원래 문자열을 Value로 하는 딕셔너리를 통해 애너그램을 그룹화 하는 문제
        딕셔너리의 Value만 모아서 반환함
        Time Complexity: O(N*K log K) (단, N은 입력 리스트 안의 문자열 개수(리스트 길이), K는 문자열 하나 당 길이)
        -> 정렬에 O(K log K)시간 소요, 정렬 작업은 리스트 안의 문자열 개수 N만큼 반복
        Space Complexity: O(N*K)
        -> 딕셔너리를 통해 원본 문자열 N개가 모두 저장됨
        """
        # collections의 defaultdict 사용하여 Key 없을 때 자동으로 빈 리스트 생성함 
        # Key: 정렬된 문자열, Value: 원래 문자열의 리스트
        anagram_groups = collections.defaultdict(list)

        # s는 입력 strs의 각 문자열
        # 모든 s에 대해 순회
        for s in strs:
            # s를 알파벳 순으로 정렬하고, Key로 쓰기 위해 튜플로 변환함 
            # sorted(s)는 각 문자를 요소로 갖는 리스트(예: ['h', 'i'])
            # 튜플로 바꿔서 Key로 쓸 수 있게 하였음
            key = tuple(sorted(s)) 
            # defaultdict 사용하므로, Key 존재 여부 확인 불필요
            # 해당 Key의 Value에 원래 문자열 s 추가
            anagram_groups[key].append(s)
        # 딕셔너리 Value만 모아 반환
        return list(anagram_groups.values())
