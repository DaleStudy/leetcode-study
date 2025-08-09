class Solution:
    """
    시간 복잡도 (Time Complexity):
    - 이 문제는 백트래킹(DFS) 기반으로 모든 가능한 조합을 탐색합니다.
    - 최악의 경우 각 조합에서 한 숫자를 여러 번 사용할 수 있으므로, 트리의 깊이는 최대 target // min(candidates)
    - 각 깊이마다 최대 len(candidates)만큼 분기 가능
    - 따라서 시간 복잡도는 지수적으로 증가: O(2^T), T = target
        (정확한 upper bound는 계산하기 어렵지만, 대략적으로는 O(2^T) 또는 O(k^T)로 볼 수 있음)

    공간 복잡도 (Space Complexity):
        - 재귀 호출의 최대 깊이: O(T), T = target (가장 작은 숫자만 반복해서 사용하는 경우)
        - 경로 저장용 리스트(nums): O(T)
        - 결과 저장용 리스트(output): 최악의 경우 모든 가능한 조합 저장 → O(number of valid combinations * 평균 길이)
        최종 공간 복잡도: **O(T + R)**,  
        T: 재귀 깊이 / R: 결과 조합 수가 클 경우 output이 차지하는 공간
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output, nums = [], []

        def dfs(start, total):
            if total > target:
                return
            if total == target:
                output.append(nums[:])
            
            for i in range(start, len(candidates)):
                nums.append(candidates[i])
                dfs(i, total + candidates[i])
                nums.pop()
        
        dfs(0, 0)
        return output
    """
    """
    2. dp
    dp[i]는 숫자들을 더해서 합이 i가 되는 모든 조합들을 저장합니다.
    dp[num - candidate]에 있는 조합에 candidate를 추가하면 num을 만들 수 있으므로 확장합니다.
    중복된 조합을 방지하기 위해 candidates를 바깥 루프에 둠 (즉, 같은 숫자를 계속 재사용하되, 이전 숫자부터 누적).
    
    시간 복잡도 (Time Complexity):
    바깥 루프: 후보 숫자만큼 → O(N)
    안쪽 루프: target까지 반복 → O(T)
    가장 안쪽 루프: dp[num - candidate]에 있는 조합들을 모두 순회 → O(A) (A는 조합 개수 및 길이에 비례)
    → 따라서 최악의 경우 O(N × T × A)

    공간 복잡도 (Space Complexity):
    dp 배열 크기: target + 1 → O(T)
    각 dp[i]에 저장된 조합 리스트들의 개수와 길이 → O(A)
    따라서 전체 공간은 O(T × A)

    Example 2의 dp 출력:

    [[[]], [], [[2]], [], [], [], [], [], []]
    [[[]], [], [[2]], [], [[2, 2]], [], [], [], []]
    [[[]], [], [[2]], [], [[2, 2]], [], [[2, 2, 2]], [], []]
    [[[]], [], [[2]], [], [[2, 2]], [], [[2, 2, 2]], [], [[2, 2, 2, 2]]]
    [[[]], [], [[2]], [[3]], [[2, 2]], [], [[2, 2, 2]], [], [[2, 2, 2, 2]]]
    [[[]], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2]], [], [[2, 2, 2, 2]]]
    [[[]], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2], [3, 3]], [], [[2, 2, 2, 2]]]
    [[[]], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2], [3, 3]], [[2, 2, 3]], [[2, 2, 2, 2]]]
    [[[]], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2], [3, 3]], [[2, 2, 3]], [[2, 2, 2, 2], [2, 3, 3]]]
    [[[]], [], [[2]], [[3]], [[2, 2]], [[2, 3], [5]], [[2, 2, 2], [3, 3]], [[2, 2, 3]], [[2, 2, 2, 2], [2, 3, 3]]]
    [[[]], [], [[2]], [[3]], [[2, 2]], [[2, 3], [5]], [[2, 2, 2], [3, 3]], [[2, 2, 3], [2, 5]], [[2, 2, 2, 2], [2, 3, 3]]]
    [[[]], [], [[2]], [[3]], [[2, 2]], [[2, 3], [5]], [[2, 2, 2], [3, 3]], [[2, 2, 3], [2, 5]], [[2, 2, 2, 2], [2, 3, 3], [3, 5]]]
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        
        for candidate in candidates:
            for num in range(candidate, target + 1):
                for combination in dp[num - candidate]:
                    dp[num].append(combination + [candidate])
        return dp[target]
