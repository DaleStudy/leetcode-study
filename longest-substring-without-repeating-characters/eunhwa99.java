import java.util.HashMap;
import java.util.Map;

class Solution {
  // 시간 복잡도: O(N)
  // 공간 복잡도: O(N)
  public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> position = new HashMap<>();
    int start = 0; // substring의 시작점
    int maxLength = 0;

    for (int idx = 0; idx < s.length(); idx++) {
      char currentChar = s.charAt(idx);

      // 같은 문자가 이미 map 에 있고, 그 문자가 현재 substring에 포함된 문자인지 확인
      if (position.containsKey(currentChar) && position.get(currentChar) >= start) {
        start = position.get(currentChar) + 1;
        // 같은 문자가 포함되지 않게 substring의 시작을 옮긴다.
      }

      maxLength = Math.max(maxLength, idx - start + 1);

      position.put(currentChar, idx);
    }

    return maxLength;
  }
}

