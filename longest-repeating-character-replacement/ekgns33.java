/**

 input : String s
 output : after k times operation, return length of longest substring
 that consist of same letters

 example
 AAAA << 4
 AAAB << AAA << 3

 constraints:
 1) input string can be empty?
 nope. at least one letter
 2) string s contains whitespace? non-alphabetical chars?
 nope. only uppercase English letters
 3) range of k?
 [0, n], when n is the length of string s

 ABAB
 AAAB
 AAAA

 AABABBA
 AAAABBA
 AABBBBA

 AABABBA
 l
 r
 count : 1
 4

 solution 1: brute force
 ds : array
 algo : for loop

 nested for loop
 iterate through the string s from index i = 0 to n
 set current character as 'target'
 set count = 0
 iterate through the string s from index j = i + 1 to n
 if next character is identical to 'target'
 continue;
 else
 increase count;

 if count > k
 break and save length

 if count <=k compare length with max
 ABAB
 i
 j
 target = A
 count = 1
 ABAB << count = 2, length = 4
 tc : O(n^2)
 sc : O(1)

 solution 2: two pointer

 AABCABBA
 l
 r
 A : 1
 B : 1
 C : 1
 count = 1
 res = 4
 set two pointer l and r
 set count to 0;
 set maxFrequency character s[0];

 move r pointer to right
 if current char is not maxFreqChar
 count + 1;
 else
 continue;

 if count > k
 while count <= k
 move leftpointer right;
 update frequency
 set max Frequency character at each iteration O(26)
 update count

 tc: O(n)
 sc : O(26) ~= O(1)
 */

class Solution {
  public int characterReplacement(String s, int k) {
    int l = 0, r = 1, maxFreq = 1, res = 1;
    int n = s.length();
    int[] freq = new int[26];
    // base case;
    char maxFreqChar = s.charAt(0);
    freq[maxFreqChar - 'A']++;
    // loop
    while (r < n) {
      char next = s.charAt(r);
      maxFreq = Math.max(maxFreq, ++freq[next - 'A']);

      while(r - l + 1 - maxFreq > k) {
        freq[s.charAt(l) - 'A']--;
        l++;
        for(int i = 0; i <26; i++) {
          if(freq[i] > maxFreq) {
            maxFreq = freq[i];
          }
        }
      }
      res = Math.max(res, r - l+1);
      r++;
    }

    return res;
  }
}
