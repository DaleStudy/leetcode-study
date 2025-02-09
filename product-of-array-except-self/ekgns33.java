/*
input : array of integer
output : array of integer that each element
     is product of all the elements except itself
constraint
1) is the result of product also in range of integer?
yes product of nums is guaranteed to fit 32-bit int
2) how about zero?
doesn't matter if the prduct result is zero
3) is input array non-empty?
yes. length of array is in range [2, 10^5]

solution1) brute force

calc all the product except current index element

tc : O(n^2) sc : O(n) << for the result. when n is the length of input array

solution 2) better?
ds : array
algo : hmmm we can reuse the product using prefix sum

1) get prefix sum from left to right and vice versa : 2-O(n) loop + 2-O(n) space
2) for i = 0 to n-1 when n is the length of input
    get product of leftPrfex[i-1] * rightPrefix[i+1]
       // edge : i == 0, i == n-1

tc : O(n) sc : O(n)

solution 3) optimal?
can we reduce space?
1) product of all elements. divide by current element.

    > edge : what if current element is zero?
    2) if there exists only one zero:
        all the elements except zero index will be zero
    3) if there exist multiple zeros:
        all the elements are zero
    4) if there is no zero
        do 1)
 */
class Solution {
  public int[] productExceptSelf(int[] nums) {
    int n = nums.length, product = 1, zeroCount = 0;
    for(int num : nums) {
      if(num == 0) {
        zeroCount ++;
        if(zeroCount > 1) break;
      } else {
        product *= num;
      }
    }

    int[] answer = new int[n];
    if(zeroCount > 1) {
      return answer;
    } else if (zeroCount == 1) {
      for(int i = 0; i < n; i++) {
        if(nums[i] != 0) {
          answer[i] = 0;
          continue;
        }
        answer[i] = product;
      }
    } else {
      for(int i = 0; i < n; i++) {
        answer[i] = product / nums[i];
      }
    }
    return answer;
  }
}
