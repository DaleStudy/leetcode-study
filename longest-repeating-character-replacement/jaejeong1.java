import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

class Solution {
  public int characterReplacement(String s, int k) {
    // 풀이: 슬라이딩 윈도우를 활용해 부분 문자열을 구한다
    // 종료 인덱스를 증가시키고, 부분 문자열 길이에서 가장 많이 들어있는 문자의 수를 뺀 값이 k보다 큰지 비교한다.
    // 크다면, 시작 인덱스를 증가시킨다.
    // 끝까지 반복하면서 최대 길이를 저장했다가 반환한다.
    // TC: O(N)
    // SC: O(N)
    var maxLength = 0;
    var start = 0;
    var end = 0;
    Map<Character, Integer> countByChar = new HashMap<>();

    while (end < s.length()) {
      countByChar.put(s.charAt(end), countByChar.getOrDefault(s.charAt(end), 0) + 1);

      while ((end - start + 1 - Collections.max(countByChar.values())) > k) {
        countByChar.put(s.charAt(start), countByChar.get(s.charAt(start)) - 1);
        start += 1;
      }
      maxLength = Math.max(end - start + 1, maxLength);
      end++;
    }

    return maxLength;
  }
}
