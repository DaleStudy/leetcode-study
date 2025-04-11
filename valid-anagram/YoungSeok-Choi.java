import java.util.HashMap;
import java.util.Map;


// NOTE: anagram 자체를 정확하게 이해하지 못해서 몇 번 틀렸던 문제.
// 두 문자열의 길이가 다르면 anagram이 아니다.
// 같은 알파뱃이 같은 개수가 있는지 확인을 하는게 문제의 핵심.

// NOTE: 시간복잡도: O(n+m)
class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        int tLen = t.toCharArray().length;
        int sLen = s.toCharArray().length;

        if(tLen != sLen) {
            return false;
        }

        for(char c: s.toCharArray()) {
            if(sMap.containsKey(c)) {
                int cnt = sMap.get(c);
                sMap.put(c, cnt + 1);
            } else {
                sMap.put(c, 1);
            }
        }

        for(char c: t.toCharArray()) {
            if(tMap.containsKey(c)) {
                int cnt = tMap.get(c);
                tMap.put(c, cnt + 1);
            } else {
                tMap.put(c, 1);
            }
        }


        for(Character c: sMap.keySet()) {
            if(!tMap.containsKey(c)) {
                return false;
            }

            int sMapCnt = sMap.get(c);
            int tMapCnt = tMap.get(c);

            if(sMapCnt != tMapCnt) {
                return false;
            }
        }

        return true;
    }
}
