import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 * Runtime: 105 ms (Beats 5.05%)
 * Memory: 46.94 MB (Beats 25.55%)
 * Space Complexity: O(1)
 * > 26개 영문자에 대한 Hash 테이블 => O(26) => O(1)
 * Time Complexity: O(N)
 * - 윈도우를 문자열 길이만큼 이동시키기 => O(N)
 * - 윈도우 변경할 때마다 최소변경필요개수 구하기 => O(26) => O(1)
 * > O(N)xO(1) => O(N)
 * 
 */
class Solution {
  /**
   * 슬라이딩 윈도우 기법 사용
   * 
   * 1. 시작인덱스, 종료인덱스 설정.
   * 2. 윈도우 안에 변경 필요 건수가 k 보다 크면 시작인덱스 늘리기 => 변환할 수 없기 때문에
   * 3. 만약 변경 필요 건수가 k와 작거나 같다면 종료인덱스 늘리기 => 변환 가능한 유효한 문자열이기 때문
   */
  public int characterReplacement(String s, int k) {
    int strIdx = 0;
    int endIdx = 0;
    int visited = -1; // visited 문자까지는 윈도우에 들어갔기 때문에 넣지 않는다.
    int ans = 0;

    // 윈도우 상태 관리
    Map<Character, Integer> winState = new HashMap<>();

    while (s.length() > endIdx) {

      // endC를 윈도우에 추가하기
      if (visited < endIdx) { // 두번 넣지 않게 방어막 쳐주기
        Character endC = Character.valueOf(s.charAt(endIdx));
        int temp = winState.getOrDefault(endC, 0);
        winState.put(endC, temp + 1);
        visited++;
      }

      // 유효성 검사하기 O(26)
      int minChng = cntMinChng(winState, endIdx - strIdx + 1);
      if (minChng <= k) { // 유효한 상태
        ans = Integer.max(ans, endIdx - strIdx + 1);
        endIdx++;
      } else { // 유효하지 않은 상태
        Character strC = Character.valueOf(s.charAt(strIdx));
        // 뒷자리 하나 빼기
        int temp = winState.getOrDefault(strC, 0);
        winState.put(strC, temp - 1);
        strIdx++;
      }
    }
    return ans;
  }

  /**
   * 시간복잡도 => O(26)
   * 윈도우에서 최소변경필요개수 카운트
   * 변경해야할 최소 값 = 현재 윈도우 길이 - (가장 많이 등장한 문자 개수)
   */
  private int cntMinChng(Map<Character, Integer> winState, int winLen) {
    int minChng = Integer.MAX_VALUE;
    Iterator<Map.Entry<Character, Integer>> it = winState.entrySet().iterator();
    // 비어 있다면 0개로 출력
    if (!it.hasNext()) {
      return 0;
    }

    // 뭔가 있으면 돌리기
    while (it.hasNext()) {
      Map.Entry<Character, Integer> entry = it.next();
      int v = entry.getValue();
      int chng = winLen - v;
      minChng = Integer.min(chng, minChng);
    }
    return minChng;
  }
}
