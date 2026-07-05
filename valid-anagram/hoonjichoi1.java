import java.util.HashMap;

public class hoonjichoi1 {
    public boolean isAnagram(String s, String t) {
        if (s.equals(t))
            return true;
        if (s.length() != t.length())
            return false;

        HashMap<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        for (int j = 0; j < t.length(); j++) {
            Character c = t.charAt(j);
            if (!map.containsKey(c) || map.get(c) <= 0) {
                return false;
            }

            map.put(c, map.get(c) - 1);
        }

        for (Integer i : map.values()) {
            if (i < 0) {
                return false;
            }
        }
        return true;
    }
}
