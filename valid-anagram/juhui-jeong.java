class Solution {
    public boolean isAnagram(String s, String t) {
        char[] charArrS = s.toCharArray();
        char[] charArrT = t.toCharArray();        
        Arrays.sort(charArrS);
        Arrays.sort(charArrT);
        return Arrays.equals(charArrS, charArrT);
    }
}
