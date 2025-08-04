/*
- 애너그램 또는 어구정철 : 문장의 순서를 바꾸어 다른 단어로 만드는 것
- 같은 단어가 맞는지 검증
- s와 t의 각 알파벳별로 한쪽은 증가, 한쪽은 감소하면서 갯수 세기
- 갯수가 0이 아닌 경우엔 서로 다른 단어이기에 false
*/
/*
Time Complexity : O(n)
Space Complexity : O(1)
*/
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for (int c : count) {
            if (c != 0)
                return false;
        }
        return true;
    }
}
