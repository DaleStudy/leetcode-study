import java.util.Arrays;

class Solution {
  public boolean isAnagram(String s, String t) {
    char[] sChar = s.toCharArray();
    char[] tChar = t.toCharArray();

    Arrays.sort(sChar);
    Arrays.sort(tChar);

    return Arrays.equals(sChar, tChar);
  }
}
