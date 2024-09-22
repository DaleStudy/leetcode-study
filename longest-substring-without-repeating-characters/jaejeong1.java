import java.util.HashSet;
import java.util.Set;

class SolutionLongestSubstring {

  public int lengthOfLongestSubstring(String s) {
    // 반복되는 문자열 중 가장 긴 문자열의 길이를 반환해라

    // s.length = 0 또는 1이면 return s.length()
    // lt = 0, rt = 1
    // s[lt] != s[rt] 이면 SubString 여부를 검사하고 True면 rt++, count++
    // s[lt] == s[rt] 이면 쌓인 카운트 정답에 적용하고 lt++, rt=lt+1, count 초기화
    // rt가 끝에 도달하면 그때까지 쌓인 정답 반환

    // TC: O(N*M), 전체 문자열 길이 N * 부분 문자열 길이 M
    // SC: O(M), 부분 문자열 생성 공간

    if (s.length() <= 1) {
      return s.length();
    }

    int lt = 0;
    int rt = lt + 1;
    int answer = 0;
    int count = 0;
    while (rt <= s.length()) {
      while (rt <= s.length() && isSubstring(s.substring(lt, rt))) {
        count++;
        rt++;
      }
      answer = Math.max(answer, count);

      lt++;
      rt = lt + 1;
      count = 0;
    }
    return answer;
  }

  // TC: O(M), 부분 문자열 str에 중복이 없는 경우 str의 길이
  // SC: O(M), 부분 문자열 str의 중복이 없는 경우 str의 길이
  private boolean isSubstring(String str) {
    Set<Character> set = new HashSet<>();
    set.add(str.charAt(0)); // 첫번째 문자는 바로 add
    // 두번째 문자부터 중복 검사 대상
    for (int i = 1; i < str.length(); i++) {
      // 중복 문자가 있거나, 공백이면 바로 false 리턴
      if (!set.add(str.charAt(i)) || str.charAt(i) == ' ') {
        return false;
      }
    }

    return true;
  }
}
