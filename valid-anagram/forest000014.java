/*
s와 t는 알파벳 소문자로만 이루어지므로, 카운팅을 위해 26개의 고정된 key를 사용하면 충분하고, 배열이 가장 간단하고 적합하다고 생각함

Runtime: 4 ms (Beats: 76.59%)
Time Complexity: O(n)

Memory: 43.04 MB (Beats: 78.65%)
Space Complexity: O(1)
*/

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] cnt = new int[26];

        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            cnt[t.charAt(i) - 'a']--;
        }

        for (int i = 0; i < 26; i++) {
            if (cnt[i] != 0)
                return false;
        }

        return true;
    }
}
