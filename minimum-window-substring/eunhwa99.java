class Solution {

  // TP: O(N+M)
  // SP: O(1)
  public String minWindow(String s, String t) {
    int[] tFreq = new int[128];
    for (char c : t.toCharArray()) {
      tFreq[c]++;
    }

    int left = 0;
    int right = 0;
    int minLen = Integer.MAX_VALUE;
    int minLeft = 0;
    int count = 0;
    int tLen = t.length();

    while (right < s.length()) {
      if (tFreq[s.charAt(right++)]-- > 0) { // tFreq[s.charAt(right++)]-- > 0 -> s.charAt(right) is in t
        count++; // s의 문자가 t에 있기 때문에 count를 증가시킨다.
      }

      if (count == tLen) {
        // 아래 while문은 left를 옮기면서 s의 문자가 t에 있는지 확인한다. (최소 길이를 찾기 위해)
        while (left < right && tFreq[s.charAt(left)] < 0) { // tFreq[s.charAt(left)] < 0 -> s.charAt(left) is not in t
          tFreq[s.charAt(left++)]++;
        }

        if (right - left < minLen) {
          minLen = right - left;
          minLeft = left;
        }
        tFreq[s.charAt(left++)]++; // left 한 칸 올리기 
        count--;
      }

    }

    return minLen == Integer.MAX_VALUE ? "" : s.substring(minLeft, minLeft + minLen);

  }
}
