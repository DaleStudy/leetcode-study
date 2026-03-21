class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").trim().toLowerCase();
        if (s.equals("")) return true;

        String[] strArr = s.split("");
        for (int i = 0; i < strArr.length/2; i++) {
            if (!strArr[i].equals(strArr[strArr.length-1-i])) return false;
        }
        return true;
    }
}
