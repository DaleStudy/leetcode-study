class Solution {
    public boolean isAnagram(String s, String t) {
        /**
            1. 문제 이해.
            - 아나그램: 문자의 순서만 바뀌었을 때 동일한 글자
            - 구성 문자와 숫자만 동일하면 아나그램
            2. 풀이 방식
            - comapre s.length() with t.length()
            - loop over s and t, count each word's character and it's count, and then save it as map(key-value pair structure)
            - compare map of s and t
            3. Complexity
            - time complexity: O(N)
            - space complexity: O(N)
        */

        if (s.length() != s.length()) return false;

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        for (char c: s.toCharArray()) {
            sMap.put(c, sMap.getOrDefault(c, 0) + 1);
        }
        for (char c: t.toCharArray()) {
            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        }

        return Objects.equals(sMap, tMap);
    }
}

