/*
start : 7:18 ~
input : String s
output : return if given s is valid palindrome
constraint:
1) valid palindrome?
    convert all uppercase letter to lowercase,
    remove non-alphanumeric chars,
    reads same forward and backward.
    ex) abba, aba, a, aacbcaa
2) length of the input string
    [1, 2*10^5]
3) does input string contains non-alphanumeric chars? such as whitespace
    yes, but only ASCII chars

-------

brute force:
read each character of input string.
create a new string that only contains
lowercase letters and numbers << O(n), when n is length of string s

create string which one is reversed. < O(n)

compare. < O(n)

time : O(n)-3loops, space : O(n)

-------
better : two-pointer

same as brute force. build new string.

use two pointer left and right

while left <= right
    if s[left] != s[right] return false;

return true;
-------
optimal :

use two pointer left and right
while left <= right
    if s[left] is non-alpha left++
    elif s[right] is non-alpha right--
    elif s[left] != s[right] return false
    else left++ right--

return true
time : O(n) space : O(1)
 */
class Solution {
  public boolean isPalindrome(String s) {
    int left = 0;
    int right = s.length() - 1;
    char leftC;
    char rightC;
    while(left <= right) {
      leftC = s.charAt(left);
      rightC = s.charAt(right);
      if(!Character.isLetterOrDigit(leftC)) {
        left++;
      } else if (!Character.isLetterOrDigit(rightC)) {
        right--;
      } else if (Character.toLowerCase(leftC) != Character.toLowerCase(rightC)) {
        return false;
      } else {
        left++;
        right--;
      }
    }
    return true;
  }
}
