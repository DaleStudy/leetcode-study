class Solution {
    public boolean containsDuplicate(int[] nums) {
        if (s.length() != t.length()) return false;
        Map<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), 0);
        }

        for (int i = 0; i < t.length(); i++) {
            if (!map.containsKey(t.charAt(i))) return false;
        }

        return true;
    }
}
