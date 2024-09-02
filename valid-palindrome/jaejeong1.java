class SolutionValidPalindrome {

  public boolean isPalindrome(String s) {
    // 대문자를 소문자로 변환
    // 영문자와 숫자만 남기고 모두 제거
    // 앞뒤로 읽어도 같은 경우 팰린드롬
    // 종류 별 처리 방법
    // 영어 대문자: 소문자로 변환
    // 공백: 무시
    // 소문자, 숫자: 통과
    // 그 외: 무시
    // 종료 조건: lt >= rt
    // 시간복잡도: O(N), 공간복잡도: O(N)
    var lt = 0;
    var rt = s.length() - 1;

    var input = s.toCharArray();

    while (lt < rt) {
      // 영문 또는 숫자일때까지 lt++
      while(!Character.isLetterOrDigit(input[lt]) && lt < input.length - 1) {
        lt++;
      }

      // 대문자면 소문자로 변환
      if (Character.isUpperCase(input[lt])) {
        input[lt] = Character.toLowerCase(input[lt]);
      }

      // 영문 또는 숫자일때까지 rt--
      while(!Character.isLetterOrDigit(input[rt]) && rt > 0) {
        rt--;
      }

      // 대문자면 소문자로 변환
      if (Character.isUpperCase(input[rt])) {
        input[rt] = Character.toLowerCase(input[rt]);
      }

      // lt, rt 범위가 겹쳤거나 lt와 rt 가 다르면 false 반환
      if (lt < rt && input[lt] != input[rt]) {
        return false;
      }

      lt++;
      rt--;
    }

    return true;
  }
}
