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
            if (map.containsKey(c)) {
                int value = map.get(c) + 1;
                map.put(c, value);
            } else {
                map.put(c, 1);
            }
        }

        for (int j = 0; j < t.length(); j++) {
            Character c2 = t.charAt(j);
            if (map.containsKey(c2)) {
                int value = map.get(c2) - 1;
                map.put(c2, value);
            } else {
                return false;
            }
        }

        for (Integer i : map.values()) {
            if (i < 0) {
                return false;
            }
        }
        return true;
    }
}
