/**
 input : integer of array
 output : return the only missing number
 constraints:
 1) is there any duplicate?
 no.
 2) range of element
 [0, n]

 solution 1)
 iterate through the array
 save to hash set
 iterate i from 0 to n
 check if exists

 tc : O(n) sc : O(n)

 solution 2)
 iterate throught the array
 add all the elements
 get sum of integer sequence 0 .. n with. n(n+1)/2
 get subtraction
 tc : O(n) sc : O(1)
 */
class Solution {
  public int missingNumber(int[] nums) {
    int sum = 0;
    int n = nums.length;
    for(int num : nums) {
      sum += num;
    }
    int totalSum = (n+1) * n / 2;
    return totalSum - sum;
  }
}
