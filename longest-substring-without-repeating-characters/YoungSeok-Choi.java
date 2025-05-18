import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int mx = 0;
        int autoIncrement = 0;
        Map<Character, Integer> map = new HashMap<>();
        Map<Integer, Character> reverseMap = new HashMap<>();

        for (char c : s.toCharArray()) {
            ++autoIncrement;
            if (map.containsKey(c)) {
                mx = Math.max(mx, map.size());

                int start = map.get(c);
                // NOTE: 중복 문자를 만나는 경우, 중복된 문자 이전에 Map에 들어온 원소는 모두 제거, (e.g. "sadvdf" 라는 입력이
                // 들어왔을 때 sad까지만 제거가 되고 v는 남아있어야 함.)
                for (int i = start; i >= 1; i--) {
                    if (reverseMap.containsKey(i)) {
                        char target = reverseMap.get(i);
                        reverseMap.remove(i);
                        map.remove(target);

                    } else {
                        break;
                    }
                }

                map.put(c, autoIncrement);
                reverseMap.put(autoIncrement, c);
            } else {
                map.put(c, autoIncrement);
                reverseMap.put(autoIncrement, c);
            }
        }

        return Math.max(mx, map.size());
    }
}
