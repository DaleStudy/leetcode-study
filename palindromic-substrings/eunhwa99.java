class Solution {
  public int countSubstrings(String s) {
    int count = 0;
    int n = s.length();

    for (int center = 0; center < 2 * n - 1; center++) {
      int left = center / 2;
      int right = left + (center % 2); // 홀/짝 팰린드롬 처리

      while (left >= 0 && right < n && s.charAt(left) == s.charAt(right)) {
        count++;
        left--;
        right++;
      }
    }

    return count;
  }
}
// Time Complexity: O(n^2)
// Space Complexity: O(1)

/*
예시: "abc"
중심이 문자일 때:
a (index 0),
b (index 1),
c (index 2)
중심이 문자 사이일 때:
between a and b
between b and c
→ 총 2 * 3 - 1 = 5개의 중심
*/

