// 풀이
// dp를 이용한 풀이
// 점화식 : dp[index] = Math.max(dp[index-1], dp[index-2] + nums[index])
// 사용되는 변수가 index-1, index-2 뿐이라 불필요한 배열을 제거하고자 함.

// TC : O(N)
// SC : O(1)

var rob = function(nums) {
  let dp = new Array(2);
  
  dp[0] = nums[0]
  // nums의 길이가 1인 경우 예외처리
  dp[1] = nums.length > 1 ? Math.max(nums[0], nums[1]) : nums[0]

  nums.forEach((num, index) => {
      if(index <= 1) return;
      
      let temp = Math.max(dp[1], dp[0] + nums[index])
      dp[0] = dp[1]
      dp[1] = temp
  })

  return dp[1]
};
