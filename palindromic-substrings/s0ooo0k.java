class Solution {
    // 팰린드롬의 경우 양쪽이 같아야 하므로, 중심을 잡고 left, right로 늘려나가는 방식
    public int countSubstrings(String s) {
        int cnt = 0;

        for(int i=0; i<s.length(); i++) {
            cnt += palindrome(s, i, i);
            cnt += palindrome(s, i, i+1);
        }
        return cnt;
    }
    public static int palindrome(final String s, int left, int right) {
        int cnt = 0;
        while(left>=0 && right < s.length() && s.charAt(left)==s.charAt(right)) {
            cnt++;
            left--;
            right++;
        }
        return cnt;
    }
}

