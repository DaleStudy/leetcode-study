/**
 input : array of integers
 output : length of the longest strictly increasing subsequence;
 example
 0 1 0 3 2 3 > 0 1 2 3  >> length : 4
 4 3 2 1 > 1 >> length : 1
 1 1 1 1 > 1 >> length : 1

 constraints :
 1) empty array allowed?
 no, at least one

 solution 1) brute force
 nested for loop
 iterate through the array from index i = 0 to n-1 when n is the lenght of input
 iterate throught the array from index j = i + 1 to n
 update current Maximum value
 if bigger than prev max value count ++
 tc : O(n^2);
 sc : O(1)

 solution 2) binary search + dp
 iterate through the array
 search from saved values.
 if current value is bigger than everything add
 else change value

 let val[i] save the smallest value of length i subsequence
 tc : O(nlogn)
 sc : O(n)

 */

class Solution {
  public int lengthOfLIS(int[] nums) {
    List<Integer> vals = new ArrayList<>();
    for(int num : nums) {
      if(vals.isEmpty() || vals.getLast() < num) {
        vals.add(num);
      } else {
        vals.set(binarySearch(vals, num), num);
      }
    }
    return vals.size();
  }
  int binarySearch(List<Integer> vals, int num) {
    int l = 0, r = vals.size()-1;
    while(l <= r) {
      int mid = (r - l) / 2+ l;
      if(vals.get(mid) == num) {
        return mid;
      } else if (vals.get(mid) > num) {
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    }
    return l;
  }
}
