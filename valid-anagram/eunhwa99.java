import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {

        // s 안의 문자들이 t 에도 동일한 횟수로 등장하는 지 확인
        if (s.length() != t.length()) return false; // 두 문자열의 길이가 다르다면 아나그램이 아니다.

        // 문자별 횟수 저장 map
        Map<Character, Integer> sAlphabetCountMap = new HashMap<>();
        for (char c : s.toCharArray()) { // 시간복잡도: O(n)
            sAlphabetCountMap.put(c, sAlphabetCountMap.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) { // 시간복잡도: O(n)
            if (!sAlphabetCountMap.containsKey(c)) return false; // s에 t가 가진 문자열이 없다면 아나그램이 아니다.

            int count = sAlphabetCountMap.get(c) - 1;
            if (count == 0) sAlphabetCountMap.remove(c);
            else sAlphabetCountMap.put(c, count);
        }

        // 모든 문자가 일치하면 해시맵이 비어 있어야 함
        return sAlphabetCountMap.isEmpty();
    }
}
