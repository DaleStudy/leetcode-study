/**
 input : String s
 output: length of the longest substring without repeating chararcters

 example)

 abccba >> abc, cba >> 3
 abcdeffg >> abcdef >> 6
 constraints
 1) length of string s?
 [0, 5 * 10^4]
 2) alphanumeric characters?
 english, digit, symbol, space. >> 256 ascii characters
  else >> hashmap

 solution1)

 iterate through string from index i = 0 to n-1
 iterate through string s from index j = i + 1, j to n
 if duplicate character comes up, then compare length
 tc : O(n^2)
 sc : O(1)

 solution 2) sliding window

 ds : array or hashmap << when character range is ascii, we can use array instead

 use two pointer l and r
 read until there is no repeating character in range [l, r]
 if duplicate exists
 move l until every character is unique
 ex)

 abaabcdef
 l
 r
 ^^    ^
 tc : O(n)
 sc : O(1)


 */

class Solution {
  public int lengthOfLongestSubstring(String s) {
    int[] freq = new int[256];
    int l = 0, r = 0;
    int n = s.length();
    int maxLength = 0;
    if(n <= 1) return n;

    while(r < n && l <= r) {
      char curC = s.charAt(r);
      freq[curC]++;
      while(l < r && freq[curC] > 1) {
        char prevC = s.charAt(l);
        freq[prevC]--;
        l++;
      }
      maxLength = Math.max(maxLength, r - l + 1);
      r++;
    }
    maxLength = Math.max(maxLength, r- l);
    return maxLength;
  }
}
