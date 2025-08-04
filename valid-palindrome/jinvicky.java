class Solution {

    /**
     * 런타임 231ms
     * [생각]
     * for문으로 알파벳, 숫자를 제외한 특수문자들을 제거한 후에 투 포인터 알고리즘으로 풀이하자.
     */
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                sb.append(c);
            }
            if (Character.isAlphabetic(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }

        int left = 0;
        int right = sb.toString().length() - 1;

        while (left <= right) {
            if (sb.toString().charAt(left) != sb.toString().charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    /**
     * 런타임 7ms
     * [생각]
     * 굳이 투 포인터로? 이미 활용중인 StringBuilder를 reverse()본과 원본을 비교하면 탐색 필요없다.
     * 또한 " " 케이스는 사전에 리턴처리한다.
     */
    public boolean isPalindrome2(String s) {
        if (s.equals(" "))
            return true;

        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' || Character.isDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }
        return sb.toString().equals(sb.reverse().toString());
    }
}
