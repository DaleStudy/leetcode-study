/**
 두 문자열 s와 t가 주어질 때 t가 s의 애너그램이라면 true, 아니면 false를 반환하세요.
 */

import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
public class Solution {

    // 2차 풀이 (맵 활용하여 시간 복잡도 줄이기, 시간복잡도: O(n))
    public boolean isAnagram(String s, String t) {

        Map<Character, Integer> charMap = new HashMap<>();

        char[] sArr = s.toCharArray();
        for (char sa : sArr) {
            charMap.put(sa, charMap.getOrDefault(sa, 0) + 1);
        }

        char[] tArr = t.toCharArray();
        for (char ta : tArr) {
            charMap.put(ta, charMap.getOrDefault(ta, 0) - 1);
        }

        for (int cnt : charMap.values()) {
            if (cnt != 0) {
                return false;
            }
        }

        return true;

    }


    // 1차 풀이 (정렬로 인해 O(n log n))
//    public boolean isAnagram(String s, String t) {
//
//        if (s.length() != t.length()) {
//            return false;
//        }
//
//        char[] sArr = s.toCharArray();
//        char[] tArr = t.toCharArray();
//
//        Arrays.sort(sArr);
//        Arrays.sort(tArr);
//
//        for (int i = 0; i < sArr.length; i++) {
//            if (sArr[i] != tArr[i]) {
//                return false;
//            }
//        }
//
//        return true;
//
//    }

}

