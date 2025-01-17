class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Intuition:
            리스트의 각 원소는 중복해서 사용할 수 있다.
            그렇다면 target은 재귀적으로 원소를 사용해서
            모든 경우의 수를 탐색한다.

        Time Complexity:
            O(N^2 log N):
                초기에 리스트의 원소를 정렬하는 데에 O(N log N)이 소요된다.
                또한, 재귀 함수는 최대 N번 호출될 수 있으며
                각 재귀 함수에서는 정렬하여 세트에 추가하는 경우
                O(N log N)이 소요되고,
                N개의 원소에 대해 for문을 반복한다.
                따라서 O(N^2 log N)의 시간복잡도가 소요된다.

        Space Complexity:
            O(N):
                최악의 경우 answer set에 대략 N개의 tuple이 저장된다.
                따라서 O(N)의 공간복잡도가 소요된다.
        """
        candidates.sort()   # O(N log N)
        answer_set = set()


        def dfs(n, arr):
            if n == 0:
                answer_set.add(tuple(sorted(arr)))  # O(N log N)
                return

            for candidate in candidates:    # O(N)
                if n >= candidate:
                    arr.append(candidate)
                    dfs(n - candidate, arr)
                    arr.pop()


        dfs(target, []) # O(N)
        answer = list(answer_set)
        return answer
