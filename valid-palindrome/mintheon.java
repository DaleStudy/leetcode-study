class Solution {
  public boolean isPalindrome(String s) {
    int start = 0;
    int end = s.length() - 1;

    while(start < end) {
      if(!Character.isLetterOrDigit(s.charAt(start))) {
        start++;
        continue;
      }

      if(!Character.isLetterOrDigit(s.charAt(end))){
        end--;
        continue;
      }

      if(Character.toLowerCase(s.charAt(start)) != Character.toLowerCase(s.charAt(end))) {
        return false;
      }

      start++;
      end--;
    }

    return true;
  }
}