class Solution:
    def traverse(self, candidates: List[int], target: int, result: List[List[int]], current: List[int], starting: int):
        # 조건을 만족하는 경우 결과에 추가하고 반환함으로써 콜 스택을 더 이상 쌓지 않음
        if target == 0:
            result.append(current[:])
            return
        
        # 아예 조건을 만족하지 않는 경우 반환함으로써 콜 스택을 더 이상 쌓지 않음
        if target < 0:
            return
        
        # starting 인덱스가 필요한 이유는, 결과 케이스의 원소 순서가 중요하지 않기 때문
        # 즉, [2, 3]과 [3, 2]가 같은 케이스이기 때문
        # 인덱스에 따른 가지치기 적용, 잠재적 중복 케이스 제거
        for i in range(starting, len(candidates)):
            candidate = candidates[i]

            # 앞서 투입했던 current 배열을 인-메모리 조작하여 원소 삽입
            current.append(candidate)

            # 콜 스택에 의해, 여기서 호출한 traverse가 먼저 result에 결과를 추가
            # 만약 이 "자식 호출"이 조건을 만족한다면, 위에서 처리하고 반환
            self.traverse(candidates, target - candidate, result, current, i)
            
            # 인-메모리 조작한 current 배열을 원상복구
            current.pop()
        
        # 모든 자식 호출을 마무리지은 traverse 함수는 None을 반환

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        current = [] # DFS 수행 중, 현재까지의 결과를 담을 배열

        self.traverse(candidates, target, result, current, 0)

        return result
