function climbStairs(n: number): number {
  /*
    * 아이디어 
    * 층수 제한: 1 <= n <= 45
    * 1 or 2 step 만 올라갈 수 있음
    
    * 1 -> [1]
    * 2 -> [1,1]              [2]                                     
    * 3 -> [1,1,1]            [2,1] [1,2]                             
    * 4 -> [1,1,1,1]          [2,1,1] [1,2,1] [1,1,2]                      [2,2]     
    * 5 -> [1,1,1,1,1]        [2,1,1,1] [1,2,1,1] [1,1,2,1] [1,1,1,2]      [2,2,1], [1,2,2], [2,1,2]
    * 6 -> [1,1,1,1,1,1]      [2,1,1,1,1] [...] [1,1,1,1,2]                [2,2,1,1], [2,1,2,1], [2,1,1,2] [1,1,2,2], [1,2,1,2], [1,2,2,1]
    =>     (1-n, 2-0) n가지   (1:n-2, 2:1) (n-1)*(n-2)/(n-2) 가지          (1: n-4, 2: n/2) (n-2)*(n-3)/2 가지   
    */

  // # solution 1
  // TC: O(N)
  // SC: O(N)
  // const stair = {1: 1, 2:2}
  // for(let i = 3; i<=n; i++){
  //     stair[i] = stair[i-1] + stair[i-2]
  // }

  // # solution 2
  // TC: O(N)
  // SC: O(1)
  //     if(n < 3) return n
  //     let curr = 2
  //     let prev = 1

  //     for(let i=0; i<n-2; i++){
  //         const next = prev + curr;
  //         prev = curr;
  //         curr = next;
  //     }

  //     return curr

  // # Solution 3: 재귀
  // TC: O(N)
  // SC: O(N)
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
}
