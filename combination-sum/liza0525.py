class Solution:
    # DFS로 문제를 푼다. 단, 가지치기 필요.
    # 이 때 가지치기를 하기 위해 candidates을 먼저 오름차순으로 sorting을 하고 (각 요소는 unique한 숫자)
    # 실제 target 숫자와 지금까지 저장해돈 target_list의 합의 대소 비교를 하며 깊이 탐색을 더 할지 말지 결정한다.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        # candidates를 먼저 sorting(문제 조건에 sort가 되어 있다는 점이 없음)
        candidates.sort()
        len_candidates = len(candidates)

        # 깊이 우선 탐색 함수
        def dfs(target_list, start_i):
            for i in range(start_i, len_candidates):
                if sum(target_list) == target:
                    # target_list를 results에 넣어준다.
                    # target_list는 리스트 객체이므로 deepcopy를 해서 넣어줘야 함
                    # 이 이상 탐색해봤자 target보다 큰 값이 나오기 때문에 탐색을 마친다.
                    results.append(target_list[:])
                    return

                if sum(target_list) + candidates[i] > target:
                    # 지금까지 쌓아온 target_list의 전체 합과 현재 인덱스의 값을 더한 것이
                    # target보다 크면 더이상 탐색하지 않아도 된다(뒤에 있는 index의 값도 다 무조건 커짐)
                    # 따라서 탐색을 마치기 위해 return한다.
                    return

                # 탐색을 계속해야 하는 경우에는 target_list에 candidate[i]의 값을 넣어준 후
                # 그 다음 깊이 탐색을 한다.
                # i번째 수보다 작은 수를 탐색할 필요가 없기 때문에 다음 탐색의 start_i로 현 시점의 i를 넣어준다.
                target_list.append(candidates[i])
                dfs(target_list, i)

                # 탐색을 끝내고 오면 pop
                target_list.pop()

        # 깊이 우선 탐색 시작
        dfs([], 0)

        return results
