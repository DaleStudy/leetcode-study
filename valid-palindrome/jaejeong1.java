class SolutionValidPalindrome {

  public boolean isPalindrome(String s) {
    // 대문자를 소문자로 변환
    // 영문자와 숫자만 남기고 모두 제거
    // 앞뒤로 읽어도 같은 경우 팰린드롬
    // 종류 별 처리 방법
    // 공백: 무시
    // 소문자, 숫자: 통과
    // 그 외: 무시
    // 종료 조건: lt >= rt
    // 시간복잡도: O(N), 공간복잡도: O(1)
    var idxLt = 0;
    var idxRt = s.length() - 1;

    char charLt;
    char charRt;

    while (idxLt < idxRt) {
      charLt = s.charAt(idxLt);
      charRt = s.charAt(idxRt);

      // 영문 또는 숫자일때까지 lt++
      while(!Character.isLetterOrDigit(charLt) && idxLt < s.length() - 1) {
        idxLt++;
        charLt = s.charAt(idxLt);
      }

      // 영문 또는 숫자일때까지 rt--
      while(!Character.isLetterOrDigit(charRt) && idxRt > 0) {
        idxRt--;
        charRt = s.charAt(idxRt);
      }

      // 대문자면 소문자로 변환 + lt, rt 범위가 겹쳤거나 lt와 rt 가 다르면 false 반환
      if (idxLt < idxRt) {
        if (Character.isUpperCase(charLt)) {
          charLt = Character.toLowerCase(charLt);
        }

        if (Character.isUpperCase(charRt)) {
          charRt = Character.toLowerCase(charRt);
        }

        if (charLt != charRt) {
          return false;
        }
      }

      idxLt++;
      idxRt--;
    }

    return true;
  }
}
