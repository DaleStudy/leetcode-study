/**
 * Constraints
 * - 1 <= s.length <= 2 * 10^5
 * - s consists only of printable ASCII characters.
 *
 * Output
 * - true : 좌우 동일
 * - false : 좌우 비동일
 */


class Solution {
    public boolean isPalindrome(String s) {

        // 해결법 1 (투포인터)
        // 시간복잡도: O(N), 공간 복잡도 : O(1)
        // 2ms & Beats 99.05%
        int left = 0, right = s.length() - 1;

        while (left < right) {
            // (1)
            if (!Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            else if (!Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            else {
                if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                    return false;
                }

                left++;
                right--;
            }


            // (2)
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }

        return true;

        // 해결법 2 (Stream API)
        // 시간 복잡도 : O(N), 공간 복잡도 : O(N)
        // 133ms & Beats 5.58%
        String filtered = s.chars()
                .filter(Character::isLetterOrDigit)
                .mapToObj(c -> String.valueOf((char) Character.toLowerCase(c)))
                .reduce("", String::concat);

        return IntStream.range(0, filtered.length() / 2)
                .allMatch(i -> filtered.charAt(i) == filtered.charAt(filtered.length() - 1 - i));
    }
}
