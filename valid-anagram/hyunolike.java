class Solution {
    public boolean isAnagram(String s, String t) {
        // 각 문자열 배열 char[] 로 변환
        // 그리고 비교 (?)

        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        Arrays.sort(sArray);
        Arrays.sort(tArray);

        return Arrays.equals(sArray, tArray);
    }
}
