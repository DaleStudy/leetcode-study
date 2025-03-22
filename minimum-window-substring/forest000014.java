/*
# Time Complexity: O(m * c)
  - c는 문자열에 사용된 문자의 가짓수(= 소문자 26 + 대문자 26)
  - 슬라이딩 윈도우로 s 전체를 훑는데 O(m)이 필요하고, 각 윈도우마다 t의 전체 문자가 포함되어 있는지 판단하는데 O(c)가 필요함
# Space Complexity: O(c)
  - sMap(슬라이딩 윈도우에 포함된 문자 카운트), tMap(문자열 t에 포함된 문자 카운트) 각각 O(c)
*/
class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            tMap.merge(t.charAt(i), 1, Integer::sum);
        }

        String ans = "";
        int ansLen = Integer.MAX_VALUE;
        int l = 0;
        int r = 0;
        sMap.merge(s.charAt(0), 1, Integer::sum);
        while (l <= r) {
            if (included(sMap, tMap)) {
                if (r - l + 1 < ansLen) {
                    ansLen = r - l + 1;
                    ans = s.substring(l, r + 1);
                }
                sMap.merge(s.charAt(l), -1, Integer::sum);
                l++;
            } else {
                r++;
                if (r >= s.length()) break;
                sMap.merge(s.charAt(r), 1, Integer::sum);
            }
        }

        while (l <= r && included(sMap, tMap)) {
            if (r - l + 1 > ansLen) {
                ansLen = r - l + 1;
                ans = s.substring(l, r + 1);
            }
            sMap.merge(s.charAt(l), -1, Integer::sum);
            l++;
        }

        return ans;
    }

    private boolean included(Map<Character, Integer> sMap, Map<Character, Integer> tMap) {
        for (Character key : tMap.keySet()) {
            if (!sMap.containsKey(key) || sMap.get(key) < tMap.get(key)) return false;
        }
        return true;
    }
}
