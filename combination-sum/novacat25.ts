/*
공간 복잡도: O(N^(T/M)) // N: candidates, T: target, M: the minimum candidate value
시간 복잡도: O(T/M)
풀이: Backtracking & Pruning 기법 활용 ([백트랙킹] 개념 추가 보충 학습 필요!)
(1) 오름차순 정렬을 수행한다. 이점은 다음과 같다.
- 후보 순서가 [2,2,..], [2,3]로 이루어지며 [3,2] 등의 불필요한 후보를 고르지 않게 할 수 있다.
- 남은 숫자가 현재 후보 값보다 작은 경우, 불필요한 탐색을 하지 않고 호출을 중단할 수 있다.
(2) remaining target이 0으로 딱 맞아떨어지는 경우 result 배열에 push하여 유효 후보를 정한다.
(3) 그 외에는 remaining 값에 현재 candidate 값을 뺀 후, idx를 유지하고 recurse를 실시한다.
(4) Backtrack하여 다음 조합을 시도한다.
*/
const combinationSum = (candidates: number[], target: number): number[][] => {
  const result: number[][] = []
  candidates.sort((a, b) => a - b)

  const backtrack = (start: number, remaining: number, current: number[]) => {
    if (remaining === 0) {
      result.push([...current])
      return
    }

    for (let i = start; i < candidates.length; i++) {
      const currentCandidate = candidates[i]
      if (currentCandidate > remaining) break
      current.push(currentCandidate)

      const substractedRemaining = remaining - currentCandidate

      backtrack(i, substractedRemaining, current)
      current.pop()
    }
  }

  backtrack(0, target, [])

  return result
}
