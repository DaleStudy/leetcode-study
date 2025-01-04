class Solution {
  /**
   시간복잡도: O(n^2)
   공간복잡도: O(1)
   -> 모든 부분 문자열을 확인하는 방식 대신 좀 더 최적화한 방식으로 다시 풀어볼 것.
   */
  public int countSubstrings(String s) {
    int count = 0;

    for(int i = 0; i < s.length(); i++) {
      for(int j = i; j < s.length(); j++) {
        if(isPalindrom(s, i, j)) {
          count++;
        }
      }
    }

    return count;
  }

  private boolean isPalindrom(String text, int left, int right) {
    while(left < right) {
      if(text.charAt(left) != text.charAt(right)) {
        return false;
      }

      left++;
      right--;
    }

    return true;
  }
}
