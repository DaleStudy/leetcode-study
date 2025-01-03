/*
input : array of integer
output : largest sum of subarray
constraints : 
1) is the input array not empty?
yes. at least one el
2) range of integers
[-10^4, 10^4]
3) maximum lenght of input
[10^5]
>> maximum sum = 10^5 * 10^4 = 10 ^ 9 < INTEGER

sol1) brute force
nested for loop : O(n^2)
tc : O(n^2), sc : O(1)

sol2) dp?
Subarray elements are continuous in the original array, so we can use dp.
let dp[i] represent the largest sum of a subarray where the ith element is the last element of the subarray.

if dp[i-1] + curval  < cur val : take curval
if dp[i-1] + cur val >= curval :  take dp[i-1] + curval
tc : O(n) sc : O(n)
 */
class Solution {
  public int maxSubArray(int[] nums) {
    int n = nums.length;
    int[] dp = new int[n];
    int maxSum = nums[0];
    dp[0] = nums[0];
    for(int i = 1; i < n; i++) {
      if(dp[i-1] + nums[i] < nums[i]) {
        dp[i] = nums[i];
      } else {
        dp[i] = nums[i] + dp[i-1];
      }
      maxSum = Math.max(maxSum, dp[i]);
    }
    return maxSum;
  }
}
