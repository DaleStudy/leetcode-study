/**
 * 시간 복잡도:
 *   text1과 text2의 길이로 구성된 2차원 매트릭스를 순회하므로,
 *   text1의 길이를 n, text2의 길이를 m이라고 하면 O(m*n)
 * 공간 복잡도:
 *   text1과 text2의 길이로 구성된 2차원 매트릭스를 생성하므로, O(m*n)
 */
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
  const dp = new Array(text1.length+1).fill(0).map(e => new Array(text2.length+1).fill(0));
  for(let i = text1.length -1; i >= 0; i--) {
      for(let j = text2.length-1; j >=0; j--) {
          if(text1[i] === text2[j]) {
              dp[i][j] = dp[i+1][j+1] + 1
          } else {
              dp[i][j] = Math.max(dp[i+1][j], dp[i][j+1])
          }
      }
  }
  return dp[0][0]
};
