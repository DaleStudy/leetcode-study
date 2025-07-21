/**
 * 도둑이 각 집에 돈의 양이 있는데, 근접한 집은 연결된 보안 시스템이 있다
 * 두 근접 집이 같은 밤에 강도당하면 경찰에게 연락감
 * 오늘 경찰에게 연락이 가지 않으면서 훔칠 수 있는 최대 돈 리턴
 */

/**
 * 만약 dfs로 구한다면, 시간복잡도는 2^n이 된다
 */
/**
 * @param {number[]} nums
 * @return {number}
 */

//최대값 즉 최적의 해를 구하는 문제. dp를 활용해보자.
var rob = function (nums) {
  //배열 크기가 늘어남에 따라, 작은 배열에 대한 결과를 활용하여 계산하는 아이디어.
  const dp = new Array(nums.length + 1); //공간복잡도 O(n)
  /**
  dp[0] = 0; //하나도 없을떄
  dp[1] = nums[0]; //집이 한곳일때
  dp[2] = Math.max(dp[1], nums[1]); //집이 한곳일때의 dp값과, 현재 순번의 돈
  dp[3] = Math.max(dp[2], dp[1] + nums[2]);// 더하지 않으면 이전 결과값, 더하려면 그 전의 결과값에 더하기
   */
  for (let i = 2; i < dp.length; i++) {
    //시간복잡도 O(n)
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i - 1]);
  }
  return dp[dp.length - 1];
};

var rob2 = function (nums) {
  //배열에 저장하지 않고 변수에 바로 담는 방식
  let prev = 0;
  let curr = 0;
  for (let num of nums) {
    //prev는 이전의 curr값으로, curr값은 이전의 prev + num
    let tempPrev = prev;
    prev = curr;
    curr = Math.max(num + tempPrev, curr);
  }
  return curr;
};
//공간복잡도를 O(1)로 개선


//7.21 풀이시간 10분 소요


/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const dp = new Array(nums.length+1).fill(0);
    dp[1] = nums[0]
    for(let i = 2; i<=nums.length;i++){
        dp[i] = Math.max(dp[i-1],dp[i-2]+nums[i-1])
    }
    return dp[nums.length]
};
/**
시간복잡도 : O(n)
공간복잡도 : O(n)
 */
