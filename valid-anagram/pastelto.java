class Solution {
    /**
     * Checks if two strings are anagrams.
     *
     * Time Complexity: O(n) - where n is the length of the string
     * Space Complexity: O(k) - where k is the number of unique characters
     *
     * @param s First string
     * @param t Second string
     * @return Return true if it is anagram
     */
    public boolean isAnagram(String s, String t) {
        // Early return if lengths differ
        if (s.length() != t.length()) return false;

        // Store character frequencies (s: +1, t: -1)
        Map<Character, Integer> count = new HashMap<>();

        // Calculate frequencies in single pass
        for (int i = 0; i < s.length(); i++) {
            count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0) + 1);
            count.put(t.charAt(i), count.getOrDefault(t.charAt(i), 0) - 1);
        }

        // All frequencies must be 0 for anagram
        for (int c : count.values()) {
            if (c != 0) return false;
        }

        return true;
    }
}

/*
 * ============================================================
 * SELF REVIEW
 * ============================================================
 * Problem: Valid Anagram
 * Date: 2025-11-18
 * Result: Accepted
 * Runtime: 25ms (Beats 6.36%)
 * Memory: 44.59MB (Beats 52.17%)
 *
 * APPROACH:
 * - HashMap을 이용한 빈도수 계산
 *
 * COMPLEXITY:
 * - Time: O(n), Space: O(k)
 *
 * KEY LEARNINGS:
 * - 해당 문제를 보자마자 HashMap을 생각했는데, 생각보다 속도 측면에서 다른 답안에 비해 매우 느렸다.
 * - 다른 방법으로 Arrays.sort(), int[] counting 방식이 있었다.
 * - 문제의 다양한 해결 방식에 대해서 공부가 필요하다.
 * ============================================================
 */