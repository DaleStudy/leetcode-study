function climbStairs(n: number): number {
  /*
    * 아이디어 
    * 층수 제한: 1 <= n <= 45
    * 1 or 2 step 만 올라갈 수 있음
    
    * 1 -> [1]
    * 2 -> [1,1]              [2]                                     
    * 3 -> [1,1,1]            [2,1] [1,2]                             
    * 4 -> [1,1,1,1]          [2,1,1] [1,2,1] [1,1,2]                            [2,2]     
    * 5 -> [1,1,1,1,1]        [2,1,1,1] [1,2,1,1] [1,1,2,1] [1,1,1,2]      [2,2,1], [1,2,2], [2,1,2]
    * 6 -> [1,1,1,1,1,1]      [2,1,1,1,1] [...] [1,1,1,1,2]                     [2,2,1,1], [2,1,2,1], [2,1,1,2] [1,1,2,2], [1,2,1,2], [1,2,2,1]
    =>     (1:n, 2:0) n가지   (1:n-2, 2:1) / n가지                         (1: n-4, 2: n/2) C(n, n/2) 가지   
    */

  // # Solution 1

  // const stair = {1: 1, 2:2}
  // for(let i = 3; i<=n; i++){
  //     stair[i] = stair[i-1] + stair[i-2]
  // }
  // TC: O(N)
  // SC: O(N)

  // # Solution 2

  //     if(n < 3) return n
  //     let curr = 2 // 현재 계단을 오르는 방법 수
  //     let prev = 1 // 이전 계단을 오르는 방법 수

  //     for(let i=0; i<n-2; i++){
  //         const next = prev + curr;
  //         prev = curr;
  //         curr = next;
  //     }

  //     return curr
  // TC: O(N)
  // SC: O(1)

  // # Solution 3: 재귀
  const memo = { 1: 1, 2: 2 };
  function calculateClimbingWay(n, memo) {
    if (!(n in memo)) {
      if (n < 3) {
        return n;
      }
      memo[n] =
        calculateClimbingWay(n - 1, memo) + calculateClimbingWay(n - 2, memo);
    }
    return memo[n];
  }
  return calculateClimbingWay(n, memo);
  // TC: O(N)
  // SC: O(N)
}
