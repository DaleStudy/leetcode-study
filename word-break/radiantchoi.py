class Solution:
    def traverse(self, s: str, wordDict: List[str], checked: int, memo: Dict[int,bool]) -> bool:
        # checked의 의미: 현재까지 체크한 문자열의 길이 - 아직 여기서부터 시작해서 끝까지 갈 수 있다고 장담할 수 없음
        # 시작 인덱스가 문자열의 길이와 같은 경우, 이 문자열에 대해 검사를 마쳤다는 뜻 (남은 길이가 0)
        if checked == len(s):
            return True

        # 지금 다루려는 인덱스를 이미 체크했다면, 후속 계산을 하지 않고 바로 반환
        if checked in memo:
            return memo[checked]

        for word in wordDict:
            # 슬라이싱 대신 startswith를 쓰는 것이 성능상 이점이 있다
            # 지금 보려는 단어가 문자열의 prefix인 경우, 즉 다음 탐색을 수행해 볼 여건이 되는 경우
            # 여기서 시작해서 끝까지 갔을 때 문장이 완성이 되니? 라는 것

            # 만약 가능할 경우, 거쳐온 모든 path에 대해 memo 딕셔너리에는 True가 저장되게 된다.
            # 또한 early return을 통해 후속 케이스를 계산하지 않는다.
            if s.startswith(word, checked):
                if self.traverse(s, wordDict, checked + len(word), memo):
                    memo[checked] = True
                    return True
        
        # 위의 for문에서 만족하는 게 없다면, 여기서 시작해가지고서는 끝까지 갈 수 없다는 것
        memo[checked] = False
        return False


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} 

        return self.traverse(s, wordDict, 0, memo)
