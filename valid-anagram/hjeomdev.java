class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        String[] sList = s.split("");
        Arrays.sort(sList);
        String[] tList = t.split("");
        Arrays.sort(tList);

        for (int i = 0; i < s.length(); i++) {
            // System.out.println(sList[i] + " " + tList[i]);
            if (!sList[i].equals(tList[i])) {
                return false;
            }
        }

        return true;
    }
}
