class Solution {
  public String minWindow(String s, String t) {
    int[] freq = new int[128];
    char[] str = s.toCharArray();
    int minL = 0;
    int minLength = Integer.MAX_VALUE;
    int l = 0, r = 0, n = s.length();
    for(char c : t.toCharArray()) {
      freq[c-'A']++;
    }
    int resolved = t.length();
    while(r < n) {
      if(freq[str[r++] - 'A']-- > 0) {
        resolved--;
      }
      while(resolved == 0) {
        if(r - l < minLength) {
          minL = l;
          minLength = r - l;
        }
        if(freq[str[l] - 'A']++ == 0) {
          resolved++;
        }
        l++;
      }
    }
    if(minLength == Integer.MAX_VALUE) return "";
    return new String(str, minL, minLength);
  }
}
