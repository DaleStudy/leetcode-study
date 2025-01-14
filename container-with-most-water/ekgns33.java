/*
input : array of integer height
output : maximum amount of water a container can store.

we can build container with two different line (height[i], height[j] when i < j)

example
1 8 6 2 5 4 8 3 7
choose i = 1.
choose j = 4
   8 ______5 
    amount of water == (j - i) * min(height[i], height[j])
   = 3 * 5 = 15

we have to maximize amount of water.

constraints:
1) is the input array valid?
length of array is in range [2, 10^5]
2) positive integers?
no. range of height is [0, 10 ^4]
>> check amount can be overflow. 10^4 * 10 ^ 5 = 10^9 < Integer range
edge:
1) if length is 2
return min(height[0], height[1]).
...

solution 1) brute force;
iterate through the array from index i = 0 to n-1
     when n is the length of input array
    iterate through the array from index j = i + 1 to n;
        calculate the amount of water and update max amount
ds : array
algo : x
tc : O(n^2) ~= 10^10 TLE
space : O(1)

solution 2) better 
ds : array
algo: two pointer?

two variant for calculating amount of water
1. height 2. width

set width maximum at first, check heights
    decrease width one by one

    - at each step width is maximum. 
        so we have to maximize
        the minimum between left and right pointer

use left and right pointer 
while left < right

    calculate amount 
    compare
    if height[left] < height[right]
        move left by one
    else 
        vice versa

return max
tc : O(n)
sc : O(1)

 */
class Solution {
  public int maxArea(int[] height) {
    int left = 0;
    int right = height.length - 1;
    int maxAmount = 0;
    while(left < right) {
      int curAmount = (right - left) * Math.min(height[left], height[right]);
      maxAmount = Math.max(maxAmount, curAmount);
      if(height[left] < height[right]) {
        left++;
      } else {
        right--;
      }
    }
    return maxAmount;
  }
}
