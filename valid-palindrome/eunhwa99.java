class Solution {

  public boolean isPalindrome(String s) {
    StringBuilder str = new StringBuilder();

    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if (Character.isLetterOrDigit(c)) {
        str.append(Character.toLowerCase(c));
      }
    }

    int left = 0, right = str.length() - 1;
    while (left < right) {
      if (str.charAt(left) != str.charAt(right)) {
        return false;
      }
      left++;
      right--;
    }

    return true;
  }
}

// 시간 복잡도 O(n) - 문자열 길이 n
// 공간 복잡도 O(1)
class newSolution {
  public boolean isPalindrome(String s) {
    int left = 0, right = s.length() - 1;

    while (left < right) {
      // 알파벳/숫자가 아닌 경우 skip
      while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
        left++;
      }
      while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
        right--;
      }

      // 소문자로 비교
      if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
        return false;
      }

      left++;
      right--;
    }
    return true;
  }
}
