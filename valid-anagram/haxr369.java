class Solution {
  /**
   * s의 문자 개수와 r의 문자 개수가 동일한지 체크
   * 배열1,2에 각각 문자 개수를 저장하기
   * a-z까지 26개
   */
  public boolean isAnagram(String s, String t) {
    /**
     * Runtime: 2 ms (Beats 98.15%)
     * Memory: 44.74 MB (Beats 38.46%)
     * Space Complexity: O(1)
     * - 26 크기의 배열 2개 사용으로 2*O(26)
     * > O(1)
     * Time Complexity: O(N)
     * - 문자열 s와 t의 문자를 하나하나 탐색 => 2*O(N)
     * - 두 문자 사용건수 저장 배열 탐색 => O(26)
     * > O(N)
     */
    int[] scount = new int[26];
    int[] tcount = new int[26];

    char A = 'a';
    for (char c : s.toCharArray()) {
      scount[c - A] += 1;
    }

    for (char c : t.toCharArray()) {
      tcount[c - A] += 1;
    }

    for (int i = 0; i < 26; i++) {
      if (scount[i] != tcount[i]) {
        return false;
      }
    }

    return true;

  }
}