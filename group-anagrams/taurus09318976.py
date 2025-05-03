'''
이 문제는 정렬된 문자열을 키(key)로 사용해 같은 애너그램끼리 그룹화함
즉, 각 단어를 정렬했을 때 같은 결과가 나오면 같은 그룹임

["eat","tea","tan","ate","nat","bat"]
단어	| 정렬 결과	| 키	| groups 딕셔너리 변화
eat	      aet	  aet	  {'aet': ['eat']}
tea	      aet	  aet	  {'aet': ['eat', 'tea']}
tan	      ant	  ant	  {'aet': [...], 'ant': ['tan']}
ate	      aet	  aet	  {'aet': ['eat','tea','ate'], ...}
nat	      ant	  ant	  {'ant': ['tan','nat'], ...}
bat	      abt	  abt	  {'abt': ['bat'], ...}

'''
class Solution:
    def groupAnagrams(self, strs: List[str]):
        groups = defaultdict(list)  # defaultdict : 키가 없어도 자동으로 빈 리스트 생성
    
        for word in strs:           # 각 단어를 하나씩 확인
            sorted_word = ''.join(sorted(word))  # 단어를 정렬해 키 생성 (예: "tea" → "aet")
            groups[sorted_word].append(word)     # 같은 키를 가진 단어를 그룹에 추가
        
        return list(groups.values())  # 그룹들을 리스트로 변환해 반환 

'''
    시간 복잡도: O(n × klogk) + O(n) = O(n × klogk)
            n: 단어 개수
            k: 단어의 최대 길이
            각 단어 정렬에 O(k log k) 시간 소요 (ex. 5글자 → 5 log 5 ≈ 11)
            단어 정렬: 각 단어를 정렬하는 데 O(k log k) 시간이 소요됩니다.
            파이썬의 sorted() 함수는 내부적으로 Timsort 알고리즘을 사용하며, 
            이의 시간 복잡도는 평균적으로 O(k log k)임
            n개의 단어 처리: 모든 단어에 대해 정렬을 수행하므로 n × O(k log k) = O(n × k log k)610.
            딕셔너리 연산: 정렬된 키를 기반으로 단어를 그룹화하는 작업은 O(1) 시간에 이루어지며, 
            전체적으로 O(n) 시간이 추가됩니다

    공간 복잡도: O(n × k) + O(n × k) = O(n × k)
            정렬된 키 저장: 각 단어를 정렬한 결과를 문자열로 저장함
                        단어 길이가 k일 때, 정렬된 문자열 저장에 O(k) 공간이 필요함
                        n개의 단어에 대해 총 O(n × k) 공간이 사용됨
            딕셔너리 값 저장: 원본 단어를 그룹별로 저장함. 모든 단어를 저장해야 하므로

'''