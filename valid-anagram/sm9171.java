class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> map = new HashMap<>();
        char[] originString = s.toCharArray();
        for (int i = 0; i < originString.length; i++) {
            Integer count = map.getOrDefault(originString[i], 0);
            map.put(originString[i], count + 1);
        }

        char[] targetString = t.toCharArray();
        for (int i = 0; i < targetString.length; i++) {
            Integer count = map.get(targetString[i]);
            if (count == null || count == 0) {
                return false;
            }
            map.put(targetString[i], count - 1);
        }
        return true;
    }
}
