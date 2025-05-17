class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 딕셔너리
        answer = {}

        for i in strs:
            key = ''.join(sorted(i))    # 정렬해서 키 만들기

            # answer에 키가 없으면 키 추가
            if key not in answer:
                answer[key] = []
            
            answer[key].append(i)   # key에 단어 추가

        # list로 변환해서 리턴
        return list(answer.values())
