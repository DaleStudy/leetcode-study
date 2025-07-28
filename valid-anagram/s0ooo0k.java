class Solution {
    /*
     * 초반 풀이시 단순 s의 문자가 t에 포함하는지만 확인하여 제대로된 비교를 못함 (ex "sass" vs "saas")
     * 따라서 정렬 후 비교하는 방식으로 전환
     * 
     * 시간복잡도 O(n log n)
     * 공간복잡도 O(n)
     */
    public boolean isAnagram(String s, String t) {
    
        if(s.length() != t.length()) 
            return false;        
        
        char[] chr1 = s.toCharArray();
        char[] chr2 = t.toCharArray();

        Arrays.sort(chr1);
        Arrays.sort(chr2);

        return Arrays.equals(chr1, chr2);
    }
}