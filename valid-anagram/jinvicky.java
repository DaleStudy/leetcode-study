import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    //유효한 애너그램의 조건이 무엇일까?
    //1. a와 b의 알파벳별 빈도수가 정확히 동일해야 한다.
    //2. 단 a와 b의 알파벳 구성 순서는 다를 수 있다.

    // map 자료구조를 활용해서 s의 알파벳 빈도수를 저장하고 이후 t를 순회하면서 map에 존재하는 알파벳일 경우
    // 1. 빈도수를 깎는다. 2. 빈도수가 0일 경우 map에서 삭제한다.
    public boolean isAnagramByHashMap(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            Integer v = map.get(c);

            if (v == null)
                return false;

            if (v - 1 == 0) {
                map.remove(c);
            } else
                map.put(c, v - 1);
        }
        return map.size() < 1;
    }

    // 또 다른 방법으로는 단순히 두 문자열을 정렬하고 문자열 내용 일치 비교를 수행하는 방법이 있다.
    // 이 방법을 사용할 때 처음에는 무조건 정렬을 수행했으나,
    // 문자열의 개수가 다르다면 1번 조건을 만족하지 못하므로 길이 비교 로직을 정렬 전에 추가함으로서 시간 성능을 높였다.
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return new String(sChars).equals(new String(tChars));
    }
}
