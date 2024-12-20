import java.util.HashSet;
import java.util.Set;

/*
start 7:06~7:14 PASS
input : integer array
output : return if input contains duplicate
constraint : 
1) empty array?
    nope. at least one 
2) size?
    [1, 10^5]
3) sorted?
    nope.
4) range of elements in the array?
    [-10^9, 10^9] >> max 2 * 10*9 +1

brute force:
ds : array. algo : just nested for-loop
iterate through the array, for index i 0 to n. n indicates the size of input
    nested loop fo r index j from i+1 to n
        if nums[j] == nums[i] return true;

return false;

time : O(n^2), space : O(1)

better:
ds : hashset. algo : one for-loop
iterate through the array:
    if set contains current value:
        return true;
    else
        add current value to set

return false;
time : O(n) space :O(n) 

 */
class Solution {
  public boolean containsDuplicate(int[] nums) {
    Set<Integer> set = new HashSet<>();
    for(int num : nums) {
      if(set.contains(num)) return true;
      set.add(num);
    }
    return false;
  }
}
