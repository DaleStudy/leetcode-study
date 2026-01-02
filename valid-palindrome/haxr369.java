/**
 * 1번 풀이가 2번 풀이를 개선한 풀이
 * 2번 풀이는 전체 조회를 2번 하지만, 1번에서는 s를 한번만 조회하고 바로 비교할 수 있게 개선.
 */
class Solution {

  /**
   * 문자열 s를 한번만 조회하면서 알파벳-숫자가 아닌 문자는 스킵하고
   * 대문자는 소문자로 변환 후 왼쪽 문자와 오른쪽 문자를 비교
   * 
   * Runtime: 1 ms (Beats 100.00%)
   * Memory: 44.24 MB (Beats 53.06%)
   * Space Complexity: O(1)
   * - 문자열 s를 순회하면서 왼쪽 오른쪽 문자, 아스키 숫자를 저장
   * > O(1)
   * Time Complexity: O(N)
   * - 문자열 s를 전체 조회 => O(N)
   * > O(N) => O(N)
   */
  public boolean isPalindrome(String s) {

    // System.out.println(buffer);
    int leftIdx = 0;
    int rightIdx = s.length() - 1;
    while (leftIdx < rightIdx) {
      char leftC = s.charAt(leftIdx);
      char rightC = s.charAt(rightIdx);
      int leftNum = (int) leftC;
      int rightNum = (int) rightC;

      // 대문자면 소문자로 변환
      if (65 <= leftNum && leftNum <= 90) {
        leftC = (char) (leftNum + 32);
      } else if (!(97 <= leftNum && leftNum <= 122) && !(48 <= leftNum && leftNum <= 57)) {
        // 알파벳, 숫자가 아닌 문자인 경우 스킵!
        leftIdx++;
        continue;
      }

      if (65 <= rightNum && rightNum <= 90) {
        rightC = (char) (rightNum + 32);
      } else if (!(97 <= rightNum && rightNum <= 122) && !(48 <= rightNum && rightNum <= 57)) {
        rightIdx--;
        continue;
      }

      if (leftC != rightC) {
        return false;
      }
      // 두 문자가 동일하면 다음 문자를 체크하기
      leftIdx++;
      rightIdx--;
    }

    return true;
  }

  /**
   * 모든 대문자를 소문자로 만들고
   * 알파벳이 아닌 문자를 다 제거한 문장이, 대칭이면 true이다. 아님 false.
   * 
   * 1. 문장을 스캔하면서 대문자는 소문자로 buffer에 넣고, 영어가 아닌 문자는 넣지 않기
   * 2. 판단할 때 아스키 코드를 이용하기
   * 
   * Runtime: 121 ms (Beats 7.53%)
   * Memory: 48.00 MB (Beats 5.23%)
   * Space Complexity: O(1)
   * - 문자열 s와 비스한 배렬(buffer)를 생성 => O(N)
   * > O(N)
   * Time Complexity: O(N)
   * - 문자열 s를 조회하면서 buffer에 붙이기 => O(N)
   * - buffer를 조회하면서 유효성 검사 => O(N)
   * > O(2N) => O(N)
   */
  public boolean isPalindrome2(String s) {
    char a = 'a'; // 97
    char z = 'z'; // 122
    char A = 'A'; // 65
    char Z = 'Z'; // 90
    char zero = '0'; // 0
    char nine = '9'; // 9

    String buffer = "";
    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if ((a <= c && c <= z) || (zero <= c && c <= nine)) {
        buffer += c;
      } else if (A <= c && c <= Z) {
        char lowerC = (char) ((int) c + 32);
        buffer += lowerC;
      }
    }

    // System.out.println(buffer);
    int leftIdx = 0;
    int rightIdx = buffer.length() - 1;
    while (leftIdx < rightIdx) {
      if (buffer.charAt(leftIdx) != buffer.charAt(rightIdx)) {
        return false;
      }
      leftIdx++;
      rightIdx--;
    }

    return true;
  }
}
