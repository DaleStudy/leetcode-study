// 시간 복잡도: O(n) - 문자열 길이 n
// 공간 복잡도: O(1) - 알파벳 개수는 26개로 고정되어 있음
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false; // 길이가 다르면 false

        int[] letterCount = new int[26];
        // 각 알파벳의 개수를 세기 위한 배열
        for(int i = 0; i < s.length(); i++){
            letterCount[s.charAt(i) - 'a']++;
            letterCount[t.charAt(i) - 'a']--;
        }

        for(int count : letterCount){
            if(count != 0) return false;
        }
        return true;

    }
}

