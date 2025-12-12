'''
문제: target이 될 때까지 candidates의 수를 더하는 모든 조합을 구하라.
풀이: 백트래킹을 이용하여 조합을 구한다. 만약 현재 합이 target과 같다면 결과 리스트에 추가하고, 작다면 후보군을 순회하며 재귀적으로 탐색한다.
시간복잡도: O(N^T), N은 후보군의 수, T는 target의 값
    최악의 경우, 후보군의 수 N과 target의 값 T에 따라 모든 조합을 탐색해야 하므로 시간복잡도는 O(N^T)이다.
공간복잡도: O(T)
    재귀 호출 스택과 현재 조합을 저장하는 데 최대 T개의 공간이 필요하므로 공간복잡도는 O(T)이다.
사용한 자료구조: 리스트
참고로 함수의 호출 깊이는 target/min(candidates)로 제한된다.
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        s, now = [], []

        def find(start, score):
            if score == target:
                s.append(now[:])
            elif score < target:
                for i in range(start, len(candidates)):
                    n = candidates[i]
                    now.append(n)
                    find(i, score+n)
                    now.pop()
        find(0, 0)
        return s
    

