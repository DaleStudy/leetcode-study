function combinationSum(candidates: number[], target: number): number[][] {
  /*
    * 합이 target이 되는 candidates 경우의 수를 리턴
    * cadidates는 고유함
    * 합이 target이 되지 않는 경우, 빈배열 리턴
    * cadidate을 중복 사용 가능
    * 2 <= candidates[i] <= 40
    * => candidate이 1인 경우는 없음
    * candidates에서 target보다 같거나 작은 값만 filter하고 시작 (target보다 큰 값은 후보군이 될 수 없음)
    * 
    
    * [2,3,6,7] / 7
    * 
    * []
    * [2] / 5
    *       [2, 2]  3 => X
    *           [2, 2, 2] 1 => X
    *               [2, 2, 2, 2] -1 => X
    *               [2, 2, 2, 3] -2 => X
    *               [2, 2, 2, 6] -5 => X
    *               [2, 2, 2, 7] -6 => X
                [2, 2, 3] 0 => O
                // ...
            [2, 3] 2 => X
                [2, 3, 2] 0 => O
                // ...
            [2, 6] -1 => X
            // ...
            
    * 
    * 하나씩 값을 추가하면서 배열의 총합을 target 값과 비교한다
    * sum이 target값보다 작으면 계속 다음 값을 추가해준다
    * sum이 target과 같으면 결과 값 result 배열에 추가해준다.
    * sum이 target보다 넘으면 마지막에 추가한 값을 뺀다.
    * 이 과정을 반복하며 배열에서 결과 값을 찾는다.
    * 
    */


      function backtrack(candidates: number[], start:number, total:number){
          if(target === total){
              result.push([...path])
              return
          }

          if(target < total){
              return
          }

          for(let i=start; i<=candidates.length-1; i++){
              path.push(candidates[i])
              backtrack(candidates, i,total + candidates[i])
              path.pop()
          }
      }

      const result = []
      const path = []
      // TC: O(NlogN)
      // SC: O(N)
      const filteredCandidates = candidates.filter(candidate => candidate<=target).sort((a,b)=> a-b)
      backtrack(filteredCandidates, 0, 0)
      return result

  };
    // TC: O(n^t) n = candidates.length, t = target 크기
    // SC: O(t)

  /*  #Solution 2 : DP
  * candidates을 가지고 target 값을 만들 수 있는 모든 조합을 미리 찾아둔다.
  *candidates [2,3,6,7] / target 7 라고 했을때
  *  1) candidate = 2
  * dp[2] = [[2]]
  * dp[4] = [[2,2]]
  * dp[6] = [[2,2,2]]
  * 2) candidate = 3
  * dp[3] = [[3]]
  * dp[5] = [[2,3]]
  * dp[6] = [[2,2,2], [3,3]]
  * dp[7] = [[2,2,3]]
  * 3) candidate = 6
  * dp[6] = [[[2,2,2], [3,3], [6]]
  * 4) candidate = 7
  * dp[7] = [[2,2,3], [7]]
  * 
  * => dp =  [
  * [ [] ]
  * [ [] ]
  * [ [2] ]
  * [[3]]
  * [[2,2]]
  * [[2,3,]]
  * [[2,2,2], [3,3], [6]]
  * [[2,2,3], [7]]
  * ]
  * ]
  * /



  // SC: O(t) t = target
  const dp = Array.from({ length: target + 1 }, () => []);
  dp[0] = [[]];


  for (let candidate of candidates) {
    for (let i = candidate; i <= target; i++) {
      for (let combination of dp[i - candidate]) {
        dp[i].push([...combination, candidate]);
      }
    }
  }

  return dp[target];
}

// TC: O(n * t * 2^n)  n = candidates.length, t = target
// SC: O((t*2^n) // 최악의 경우 모든 조합(2^n) 저장 가능
