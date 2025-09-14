import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * 초기에 중복체크를 위해 HashSet으로 풀었다가 예외 케이스가 발생해서 이전 문자의 인덱스 위치를 알아야 함을 깨닫고
     * HashMap으로 문자:인덱스 쌍을 저장했다.
     * 자료구조와 반복문의 흐름은 맞았으나 중복 발견 시 left를 Math.max()로 2가지 케이스를 모두 비교하지 않아서 문제 발생
     * 기존 left와 해당 문자의 마지막 인덱스 중 더 큰값을 선택한다.
     */
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.isEmpty()) return 0;

        Map<Character, Integer> last = new HashMap<>();
        int left = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);

            // VIP:: left를 오른쪽으로 밀거나(left+=) left를 유지한다.
            // 왜 left를 가능한 한 오른쪽으로 업데이트할까? -> 그래야 중복 제거된 온전한 슬라이딩 윈도우를 유지할 수 있기 때문이다.
            // abba의 경우 두번째 b, 두번째 a가 이에 해당한다.
            // last(b) = max(0, 1+1=2) -> 2
            // last(a) = max(2, 0+1=1) -> 2
            if (last.containsKey(ch)) {
                left = Math.max(left, last.get(ch) + 1);
            }
            maxLen = Math.max(maxLen, right - left + 1);
            last.put(ch, right); // 방금 문자의 '마지막 위치' 갱신
        }
        return maxLen;
    }
}
