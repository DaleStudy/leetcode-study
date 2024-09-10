/**
 *  시간 복잡도: O(n)
 *    - 정규식을 통해 Alphanumeric 만 남기기. -> O(n)
 *    - 소문자로 변환 -> O(n)
 *    - 투 포인터를 이용하기 때문에 -> O(n/2)
 *  공간 복잡도: O(n)
 */
class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        char[] c = s.toCharArray();

        int left = 0;
        int right = c.length - 1;

        while (left < right) {
            if (c[left++] != c[right--]) {
                return false;
            }
        }
        return true;
    }
}
