class Solution {
  public int maxProduct(int[] nums) {
    int n = nums.length;
    int[][] product = new int[2][n];
    product[0][0] = nums[0];
    product[1][0] = nums[0];
    int max = nums[0];
    for(int i = 1; i < n; i++) {
      product[0][i] = Math.max(product[0][i-1]*nums[i], Math.max(nums[i], nums[i] * product[1][i-1]));
      product[1][i] = Math.min(product[0][i-1]*nums[i], Math.min(nums[i], nums[i] * product[1][i-1]));
      max =Math.max(max, product[0][i]);
    }
    return max;
  }
}
/**


 brute force :
 nested for loop
 tc : O(n^2)
 sc : O(1)

 better sol :
 maintain min and max
 tc : O(n)
 sc : O(n)

 compare with prev Min * cur, prevMax * cur, cur
 we have to keep track of minimum value that can lead to maximum value
 when there are negative values later.

 2 3  -2 4
 2 6  -2   4
 2 2 -12 -48

 -2  0 -1
 -2  0  0
 -2  0 -1

 2 3 -2  5     7   -100
 2 6 -2  5    35   210000
 2 3 -6 -30 -210.    -35

 */
