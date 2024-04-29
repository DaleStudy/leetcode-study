class Solution {
    /**
     * 팰린드롬
     * 1. 소문자로 변환
     * 2. 영어를 제외한 문자는 제거
     * 3. 앞으로 읽어도 뒤로 읽어도 (우영우?) 똑같으면 팰린드롬 이다.
     *
     * 시간복잡도는 O(n)으로 생각된다.
     * 공간복잡도는 O(n)으로 생각된다.
     * @param s
     * @return
     */
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("[^a-z0-9]", "");
        StringBuilder sb = new StringBuilder(s);
        String reversString = sb.reverse().toString();

        return s.equals(reversString);
    }
}
